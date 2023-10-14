from Structures.User import *
from Structures.Tree import *
from Structures.MBR import *
from typing import List
from Env.Env import *
import datetime
import re

class Login:
    def setParams(self, params: dict):
        self.params = params

    def exec(self):
        if self.__validateParams():
            return self.__login()
        else:
            return self.__getError(' -> Error login: Faltan parámetros obligatorios para iniciar sesión')

    def __login(self):
        if not currentLogged['User']:
            match = re.match(r'(\d+)([a-zA-Z]+\d*)', self.params['id'])
            if match.group(2) in disks:
                if self.params['id'] in disks[match.group(2)]['ids']:
                    absolutePath = disks[match.group(2)]['path']
                    namePartition = disks[match.group(2)]['ids'][self.params['id']]['name']
                    with open(absolutePath, 'rb') as file:
                        readed_bytes = file.read(127)
                        mbr = MBR.decode(readed_bytes)
                        for i in range(len(mbr.partitions)):
                            if mbr.partitions[i].status and mbr.partitions[i].name.strip() == namePartition:
                                file.seek(mbr.partitions[i].start)
                                superBlock = SuperBlock.decode(file.read(SuperBlock.sizeOf()))
                                tree: Tree = Tree(superBlock, file)
                                content, founded = tree.readFile('/users.txt')
                                if founded:
                                    user: User = self.__isValidUser(content, self.params['user'], self.params['pass'])
                                    if user:
                                        currentLogged['User'] = User(user.id, user.group, user.name, user.password)
                                        currentLogged['Partition'] = namePartition
                                        currentLogged['PathDisk'] = absolutePath
                                        currentLogged['IDPart'] = self.params['id']
                                        return self.__getSuccess(f' -> login: Sesión iniciada exitosamente. ({user.name})')
                                    else:
                                        return self.__getError(f' -> Error login: El usuario {self.params["user"]} no existe en el sistema.')
                                return self.__getError(f' -> Error login: No existe el archivo /users.txt.')
                else:
                    return self.__getError(f' -> Error login: No existe el código de partición {self.params["id"]} en el disco {match.group(2)} para iniciar sesión.')
            else:
                return self.__getError(f' -> Error login: No existe el disco {match.group(2)}.')
        else:
            return self.__getError(f' -> Error login: Hay un usuario loggeado actualmente')

    def __isValidUser(self, content, user, password) -> User:
        users: list[User] = self.__getUsers(content)
        for u in users:
            if u.name == user and u.password == password:
                return u
        return None

    def __getUsers(self, content) -> List[User]:
        users: list[User] = []
        registers = [[j.strip() for j in i.split(',')] for i in content.split('\n') if i.strip() != '']
        for reg in registers:
            if reg[1] == 'U' and reg[0] != '0':
                users.append(User(reg[0], reg[2], reg[3], reg[4]))
        return users

    def __validateParams(self):
        if 'user' in self.params and 'pass' in self.params and 'id' in self.params:
            return True
        return False

    def __getError(self, text):
        return f"{text}"

    def __getSuccess(self, text):
        return f"{text}"