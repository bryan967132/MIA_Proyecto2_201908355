from Structures.Tree import *
from Structures.MBR import *
from Env.Env import *
import datetime
import os

class Mkfile:
    def setParams(self, params: dict):
        self.params = params

    def exec(self):
        if currentLogged['User']:
            if self.__validateParams():
                with open(currentLogged['PathDisk'], 'rb') as file:
                    readed_bytes = file.read(127)
                    mbr = MBR.decode(readed_bytes)
                    for i in range(len(mbr.partitions)):
                        if mbr.partitions[i].status and mbr.partitions[i].name.strip() == currentLogged['Partition']:
                            file.seek(mbr.partitions[i].start)
                            superBlock = SuperBlock.decode(file.read(SuperBlock.sizeOf()))
                            tree: Tree = Tree(superBlock, file)
                            disk = disks[os.path.basename(currentLogged['PathDisk']).split('.')[0]]
                            dirExists = disk['ids'][currentLogged['IDPart']]['mkdirs']
                            content = ''
                            if 'size' in self.params:
                                self.params['size'] = int(self.params['size'])
                                if self.params['size'] >= 0:
                                    while len(content) < int(self.params['size']):
                                        content += '0123456789'
                                    content = content[:int(self.params['size'])]
                                else:
                                    return self.__getError(f" -> Error mkfile: No se creó el archivo '{self.params['path']}', el atributo size debe ser un número positivo.")
                            elif 'cont' in self.params:
                                self.params['cont'] = self.params['cont'].replace('"', '')
                                abspath = os.path.abspath(self.params['cont'])
                                if os.path.isfile(abspath) and os.path.exists(abspath):
                                    content = open(abspath, 'r', encoding='utf-8').read().replace('>', '&gt;').replace('<', '&lt;')
                                else:
                                    return self.__getError(f" -> Error mkfile: No se creó el archivo '{self.params['path']}', el atributo cont no contiene una ruta de archivo válida.")
                            if self.params['path'] in dirExists:
                                return self.__getError(f" -> Error mkfile: No se creó el archivo '{self.params['path']}' porque ya existe.")
                            if self.params['r']:
                                dir = [i for i in self.params['path'].split('/') if i != '']
                                c = 1
                                while c < len(dir):
                                    tmpDir = [dir[i] for i in range(c)]
                                    if not tree.searchdir('/' + '/'.join(tmpDir)):
                                        tree.mkdir('/' + '/'.join(tmpDir), currentLogged['PathDisk'])
                                    c += 1
                                tree.mkfile(self.params['path'], currentLogged['PathDisk'])
                            else:
                                dir = [i for i in self.params['path'].split('/') if i != '']
                                if len(dir) > 1:
                                    tmpDir = [dir[i] for i in range(len(dir) - 1)]
                                    if not tree.searchdir('/' + '/'.join(tmpDir)) and len([i for i in self.params['path'].split('/') if i != '']) > 1:
                                        return self.__getError(f" -> Error mkfile: No se creó el archivo '{self.params['path']}', no existe la ruta donde intentó crearse.")
                                tree.mkfile(self.params['path'], currentLogged['PathDisk'])
                            if superBlock.filesystem_type == 3:
                                file.seek(mbr.partitions[i].start + SuperBlock.sizeOf())
                                for r in range(superBlock.inodes_count):
                                    readed_bytes = file.read(Journal.sizeOf())
                                    if readed_bytes == Journal.sizeOf() * b'\x00':
                                        with open(currentLogged['PathDisk'], 'r+b') as file:
                                            file.seek(mbr.partitions[i].start + SuperBlock.sizeOf() + r * Journal.sizeOf())
                                            file.write(Journal('mkfile', f'{self.params["path"]}', '', datetime.datetime.now()).encode())
                                            break
                            if content != '':
                                tree.writeFile(self.params['path'], currentLogged['PathDisk'], mbr.partitions[i].start, content)
                            tree.writeInDisk(currentLogged['PathDisk'], mbr.partitions[i].start, superBlock.encode())
                            dirExists.append(self.params['path'])
                            return self.__getSuccess(f' -> mkfile: Nuevo archivo creada exitosamente \'{self.params["path"]}\'')
            else:
                return self.__getError(f" -> Error mkfile: Faltan parámetros obligatorios para crear un directorio.")
        else:
            return self.__getError(f" -> Error mkfile: No hay ningún usuario loggeado actualmente.")

    def __validateParams(self):
        if 'path' in self.params:
            self.params['path'] = self.params['path'].replace('"', '')
            return True
        return False

    def __getError(self, text):
        return f"{text}"

    def __getSuccess(self, text):
        return f"{text}"