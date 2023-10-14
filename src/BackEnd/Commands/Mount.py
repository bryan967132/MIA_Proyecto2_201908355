from Structures.ListEBR import ListEBR
from Structures.MBR import *
from Structures.EBR import *
from io import BufferedRandom
from typing import List
from Env.Env import *
import os

class Mount:
    def setParams(self, params : dict):
        self.params = params

    def exec(self):
        if self.__validateParams():
            return self.__mount()
        elif self.__validateEmptyParams():
            return self.__viewMounteds()
        else:
            return self.__getError(' -> Error mount: Faltan parámetros obligatorios para montar la partición')

    def __mount(self):
        self.params['path'] = self.params['path'].replace('"', '')
        absolutePath = os.path.abspath(self.params['path'])
        if not os.path.exists(absolutePath):
            return self.__getError(f' -> Error mount: No existe el disco {os.path.basename(absolutePath).split(".")[0]} para montar la partición.')
        with open(absolutePath, 'rb') as file:
            readed_bytes = file.read(127)
            mbr = MBR.decode(readed_bytes)
            for i in range(len(mbr.partitions)):
                if mbr.partitions[i].status and mbr.partitions[i].name.strip() == self.params['name']:
                    if mbr.partitions[i].status == '0':
                        with open(absolutePath, 'r+b') as file:
                            file.seek(19 + i * 27)
                            file.write('1'.encode('utf-8'))
                        thisDisk = disks[os.path.basename(absolutePath).split('.')[0]]
                        newID = f'55{thisDisk["nextId"]}' + os.path.basename(absolutePath).split(".")[0]
                        thisDisk['ids'][newID] = {'name': self.params["name"], 'mkdirs': []}
                        thisDisk['nextId'] += 1
                        return self.__getSuccess(os.path.basename(absolutePath).split('.')[0], self.params['name'], newID, mbr.partitions[i].type)
                    return self.__getError(f' -> Error mount: Intenta montar la partición en {os.path.basename(absolutePath).split(".")[0]} que ya está montada. ({self.params["name"]})')
            i = self.__getExtended(mbr.partitions)
            if i != -1:
                listEBR: list[EBR] = self.__getListEBR(mbr.partitions[i].start, mbr.partitions[i].size, file).getIterable()
                for ebr in listEBR:
                    if ebr.name and ebr.name.strip() == self.params['name']:
                        if ebr.status == '0':
                            with open(absolutePath, 'r+b') as file:
                                file.seek(ebr.start)
                                file.write('1'.encode('utf-8'))
                            thisDisk = disks[os.path.basename(absolutePath).split(".")[0]]
                            newID = f'55{thisDisk["nextId"]}' + os.path.basename(absolutePath).split(".")[0]
                            thisDisk['ids'][newID] = {'name': self.params["name"], 'mkdirs': []}
                            thisDisk['nextId'] += 1
                            return self.__getSuccess(os.path.basename(absolutePath).split('.')[0], self.params['name'], newID, 'L')
                        return self.__getError(f' -> Error mount: Intenta montar la partición en {os.path.basename(absolutePath).split(".")[0]} que ya está montada. ({self.params["name"]})')
            return self.__getError(f' -> Error mount: Intenta montar una partición inexistente en {os.path.basename(absolutePath).split(".")[0]}.')

    def __getListEBR(self, start: int, size: int, file: BufferedRandom) -> ListEBR:
        listEBR: ListEBR = ListEBR(start, size)
        file.seek(start)
        ebr = EBR.decode(file.read(30))
        listEBR.insert(ebr)
        while ebr.next != -1:
            file.seek(ebr.next)
            ebr = EBR.decode(file.read(30))
            listEBR.insert(ebr)
        return listEBR

    def __getExtended(self, partitions: List[Partition]):
        for i in range(len(partitions)):
            if partitions[i].type == 'E':
                return i
        return -1

    def __validateParams(self):
        if 'path' in self.params and 'name' in self.params:
            return True
        return False

    def __validateEmptyParams(self):
        if len(self.params) == 0:
            return True
        return False

    def __viewMounteds(self):
        if len(disks) > 0:
            response = ' -> mount:'
            response += f'\n\t -> Particiones Montadas'
            for k, v in disks.items():
                for k1, v1 in v['ids'].items():
                    response += '\n\t -> {:<20} {:<20} {:<20}'.format(k1, v1, k)
            return response
        else:
            return f' -> mount: No hay particiones montadas.'

    def __getError(self, text):
        return f"{text}"

    def __getSuccess(self, diskname, name, newID, type):
        type = "PRIMARIA " if type == 'P' else ("EXTENDIDA" if type == 'E' else "LOGICA   ")
        return f" -> mount: Partición montada exitosamente en {diskname}. {type} ({name}: {newID})"