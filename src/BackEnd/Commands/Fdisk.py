from Structures.ListEBR import ListEBR
from Structures.MBR import *
from Structures.EBR import *
from Env.Env import *
from io import BufferedRandom
from typing import List
import os

class Fdisk:
    def setParams(self, params: dict):
        self.params = params

    def exec(self):
        if self.__validateParams():
            return self.__createPartition()
        else:
            return self.__getError(' -> Error fdisk: Faltan parámetros obligatorios para crear la partición.')

    def __createPartition(self):
        self.params['path'] = self.params['path'].replace('"', '')
        self.params['fit'] = self.params['fit'].upper()
        self.params['type'] = self.params['type'].upper()
        absolutePath = os.path.abspath(self.params['path'])
        if not os.path.exists(absolutePath):
            return self.__getError(f' -> Error fdisk: No existe {os.path.basename(absolutePath).split(".")[0]} para particionar.')
        self.params['unit'] = self.params['unit'].upper()
        if self.params['size'] < 0:
            return self.__getError(' -> Error: El tamaño de la partición debe ser mayor que cero')
        units = 1
        if self.params['unit'] == 'M':
            units = 1024 * 1024
        elif self.params['unit'] == 'K':
            units = 1024
        elif self.params['unit'] == 'B':
            units = 1
        else:
            return self.__getError(' -> Error fdisk: Unidad de Bytes Incorrecta.')
        with open(absolutePath, 'rb') as file:
            readed_bytes = file.read(127)
            mbr = MBR.decode(readed_bytes)
            if self.params['type'] != 'L' and self.__thereAreFour(mbr.partitions):
                return self.__getError(f' -> Error fdisk: Ya existen 4 particiones en el disco {os.path.basename(absolutePath).split(".")[0]}.')
            if self.__thereIsNameR(self.params['name'], mbr.partitions):
                return self.__getError(f' -> Error fdisk: Ya existe una partición con el nombre {self.params["name"]} en el disco {os.path.basename(absolutePath).split(".")[0]}.')
            self.params['fit'] = self.params['fit'][:1]
            if self.params['type'] == 'P' or self.params['type'] == 'E':
                disponible = []
                lastNoEmptyByte = 126
                for i in range(len(mbr.partitions)):
                    if mbr.partitions[i].status:
                        if mbr.partitions[i].start - lastNoEmptyByte > 2 and mbr.partitions[i].start - lastNoEmptyByte >= self.params['size'] * units + 1:
                            disponible.append([lastNoEmptyByte + 1, mbr.partitions[i].start - lastNoEmptyByte])
                        lastNoEmptyByte = mbr.partitions[i].start + mbr.partitions[i].size - 1
                if mbr.size - lastNoEmptyByte  > 2 and mbr.size - lastNoEmptyByte >= self.params['size'] * units + 1:
                    disponible.append([lastNoEmptyByte + 1, mbr.size - lastNoEmptyByte - 1])
                if len(disponible) > 0:
                    if mbr.fit == 'B':
                        disponible = self.__sortBestFit(disponible)
                    elif mbr.fit == 'W':
                        disponible = self.__sortWorstFit(disponible)
                    if self.params['type'] == 'E' and self.__getExtended(mbr.partitions) != -1:
                        return self.__getError(f' -> Error fdisk: Ya existe una partición extendida en {os.path.basename(absolutePath).split(".")[0]}.')
                    for i in range(len(mbr.partitions)):
                        if not mbr.partitions[i].status:
                            mbr.partitions[i] = Partition(
                                '0',
                                self.params['type'],
                                self.params['fit'],
                                disponible[0][0],
                                self.params['size'] * units,
                                self.params['name'][:16].ljust(16)
                            )
                            mbr.partitions = self.__sortOrder(mbr.partitions)
                            with open(absolutePath, 'r+b') as file:
                                file.seek(0)
                                file.write(mbr.encode())
                                if self.params['type'] == 'E':
                                    file.seek(mbr.partitions[i].start)
                                    file.write(EBR().encode())
                            return self.__getSuccessCreate(os.path.basename(absolutePath).split(".")[0], self.params["name"], self.params['type'], self.params["size"], self.params["unit"])
                    return self.__getError(f' -> Error fdisk: No pueden crearse mas particiones en {os.path.basename(absolutePath).split(".")[0]}.')
                else:
                    return self.__getError(f' -> Error fdisk: No hay espacio suficiente para la nueva partición en {os.path.basename(absolutePath).split(".")[0]}.')
            elif self.params['type'] == 'L':
                i = self.__getExtended(mbr.partitions)
                if i != -1:
                    listEBR: ListEBR = self.__getListEBR(mbr.partitions[i].start, mbr.partitions[i].size, file)
                    if self.__thereIsNameRL(self.params['name'], listEBR.getIterable()):
                        return self.__getError(f' -> Error fdisk: Ya existe una partición con el nombre {self.params["name"]} en el disco {os.path.basename(absolutePath).split(".")[0]}.')
                    disponible = listEBR.searchEmptySpace(self.params['size'] * units)
                    if len(disponible) > 0:
                        if mbr.partitions[i].fit == 'B':
                            disponible = self.__sortBestFit(disponible)
                        elif mbr.partitions[i].fit == 'W':
                            disponible = self.__sortWorstFit(disponible)
                        ebr = EBR(
                            status = '0',
                            fit = self.params['fit'],
                            start = disponible[0][0],
                            size = self.params['size'] * units,
                            name = self.params['name'][:16].ljust(16)
                        )
                        listEBR.insert(ebr)
                        with open(absolutePath, 'r+b') as file:
                            for e in listEBR.getIterable():
                                file.seek(e.start if e.start else mbr.partitions[i].start)
                                file.write(e.encode())
                        return self.__getSuccessCreate(os.path.basename(absolutePath).split(".")[0], self.params["name"], self.params['type'], self.params["size"], self.params["unit"])
                    return self.__getError(f' -> Error fdisk: No hay espacio suficiente para la nueva partición en {os.path.basename(absolutePath).split(".")[0]}.')
                return self.__getError(f' -> Error fdisk: No existe una partición extendida en {os.path.basename(absolutePath).split(".")[0]} para crear la partición lógica.')

    def __thereAreFour(self, partitions: List[Partition]) -> bool:
        for i in partitions:
            if not i.status:
                return False
        return True

    def __thereIsNameR(self, name: str, partitions: List[Partition]) -> bool:
        for i in partitions:
            if i.status and i.name.strip() == name:
                return True
        return False

    def __thereIsNameRL(self, name: str, partitions: List[EBR]) -> bool:
        for i in partitions:
            if i.status and i.name.strip() == name:
                return True
        return False

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

    def __sortBestFit(self, disponible):
        if len(disponible) > 1:
            for i in range(1, len(disponible)):
                for j in range(i, 0, -1):
                    if disponible[j][1] < disponible[j - 1][1]:
                        disponible[j], disponible[j - 1] = disponible[j - 1], disponible[j]
                        continue
                    break
        return disponible

    def __sortWorstFit(self, disponible):
        if len(disponible) > 1:
            for i in range(1, len(disponible)):
                for j in range(i, 0, -1):
                    if disponible[j][1] > disponible[j - 1][1]:
                        disponible[j], disponible[j - 1] = disponible[j - 1], disponible[j]
                        continue
                    break
        return disponible

    def __sortOrder(self, partitions):
        for i in range(1, len(partitions)):
            if partitions[i].start:
                for j in range(i, 0, -1):
                    if partitions[j].start < partitions[j - 1].start:
                        partitions[j], partitions[j - 1] = partitions[j - 1], partitions[j]
                        continue
                    break
                continue
            break
        return partitions

    def __validateParams(self):
        if 'size' in self.params and 'path' in self.params and 'name' in self.params:
            self.params['size'] = int(self.params['size'])
            return True
        return False

    def __getError(self, text):
        return f"{text}"

    def __getSuccessCreate(self, diskname, name, type, size, unit):
        type = "Primaria" if type == 'P' else ("Extendida" if type == 'E' else "Logica")
        unit = unit if unit in ['K', 'M'] else ""
        return " -> fdisk: Partición creada exitosamente en {}. {:<9} ({}: {} {}B)".format(diskname, type.upper(), name, size, unit)

    def __str__(self) -> str:
        return 'Fdisk'