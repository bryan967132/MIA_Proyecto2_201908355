from Structures.Tree import *
from Structures.MBR import *
from Env.Env import *
import datetime
import os

class Mkusr:
    def setParams(self, params: dict):
        self.params = params

    def exec(self):
        if currentLogged['User']:
            if currentLogged['User'].name == 'root':
                if self.__validateParams():
                    if len(self.params['user']) <= 10:
                        if len(self.params['pass']) <= 10:
                            if len(self.params['grp']) <= 10:
                                with open(currentLogged['PathDisk'], 'rb') as file:
                                    readed_bytes = file.read(127)
                                    mbr = MBR.decode(readed_bytes)
                                    for i in range(len(mbr.partitions)):
                                        if mbr.partitions[i].status and mbr.partitions[i].name.strip() == currentLogged['Partition']:
                                            file.seek(mbr.partitions[i].start)
                                            superBlock = SuperBlock.decode(file.read(SuperBlock.sizeOf()))
                                            tree: Tree = Tree(superBlock, file)
                                            content, exists = tree.readFile('/users.txt')
                                            if exists:
                                                users = tree.getUsers(content)
                                                groups = tree.getGroups(content)
                                                for u in users:
                                                    if u.name.strip() == self.params['user']:
                                                        return self.__getError(f" -> Error mkusr: Ya existe un usuario {self.params['user']}.")
                                                if not self.__existGrp(groups):
                                                    return self.__getError(f" -> Error mkusr: No existe un grupo {self.params['grp']}.")
                                                newUser: str = '{},U,{:<10},{:<10},{:<10}\n'.format(int(users[-1].id) + 1, self.params['grp'], self.params['user'], self.params['pass'])
                                                tree.writeFile('/users.txt', currentLogged['PathDisk'], mbr.partitions[i].start, newUser)
                                                return self.__getSuccess(' -> mkusr: Usuario {:<10} creado exitosamente. ({}: {})'.format(self.params['user'], currentLogged['Partition'], os.path.basename(currentLogged['PathDisk']).split('.')[0]))
                                            else:
                                                return self.__getError(f" -> Error mkusr: No existe el archivo /users.txt.")
                            else:
                                return self.__getError(f" -> Error mkusr: El nombre de grupo no puede contener más de 10 caracteres.")
                        else:
                            return self.__getError(f" -> Error mkusr: La contraseña no puede contener más de 10 caracteres.")
                    else:
                        return self.__getError(f" -> Error mkusr: El nombre de un usuario no puede contener más de 10 caracteres.")
                else:
                    return self.__getError(f" -> Error mkusr: Faltan parámetros obligatorios para crear un usuario.")
            else:
                return self.__getError(f" -> Error mkusr: Solo el usuario 'root' puede crear usuarios.")
        else:
            return self.__getError(f" -> Error mkusr: No hay ningún usuario loggeado actualmente.")

    def __existGrp(self, groups):
        for g in groups:
            if g.group.strip() == self.params['grp']:
                return True
        return False

    def __validateParams(self):
        if 'user' in self.params and 'pass' in self.params and 'grp' in self.params:
            return True
        return False

    def __getError(self, text):
        return f"{text}"

    def __getSuccess(self, text):
        return f"{text}"