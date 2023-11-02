from Structures.Tree import *
from Structures.MBR import *
from Env.Env import *
import datetime
import os

class Mkgrp:
    def setParams(self, params: dict):
        self.params = params

    def exec(self):
        if currentLogged['User']:
            if currentLogged['User'].name == 'root':
                if self.__validateParams():
                    if len(self.params['name']) <= 10:
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
                                        groups = tree.getGroups(content)
                                        newGroup: str = '{},G,{:<10}\n'.format(int(groups[-1].id) + 1, self.params['name'])
                                        tree.writeFile('/users.txt', currentLogged['PathDisk'], mbr.partitions[i].start, newGroup)
                                        return self.__getSuccess(' -> mkgrp: Grupo {:<10} creado exitosamente. ({}: {})'.format(self.params['name'], currentLogged['Partition'], os.path.basename(currentLogged['PathDisk']).split('.')[0]))
                                    else:
                                        return self.__getError(f" -> Error mkgrp: No existe el archivo /users.txt.")
                    else:
                        return self.__getError(f" -> Error mkgrp: El nombre de un grupo no puede contener más de 10 caracteres.")
                else:
                    return self.__getError(f" -> Error mkgrp: Faltan parámetros obligatorios para crear un grupo.")
            else:
                return self.__getError(f" -> Error mkgrp: Solo el usuario 'root' puede crear grupos.")
        else:
            return self.__getError(f" -> Error mkgrp: No hay ningún usuario loggeado actualmente.")

    def __validateParams(self):
        if 'name' in self.params:
            return True
        return False

    def __getError(self, text):
        return f"{text}"

    def __getSuccess(self, text):
        return f"{text}"