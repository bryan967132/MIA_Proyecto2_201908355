from Structures.MBR import *
from Env.Env import *
import os

class Mkdisk:
    def setParams(self, params: dict):
        self.params = params

    def exec(self):
        if self.__validateParams():
            self.params['unit'] = self.params['unit'].upper()
            self.params['fit'] = self.params['fit'].upper()
            if self.params['size'] < 0:
                return self.__getError(' -> Error: El tamaño de la partición debe ser mayor que cero')
            units = 1
            if self.params['unit'] == 'M':
                units = 1024 * 1024
            elif self.params['unit'] == 'K':
                units = 1024
            else:
                return self.__getError(' -> Error mkdisk: Unidad de Bytes Incorrecta')
            self.params['path'] = self.params['path'].replace('"', '')
            absolutePath = os.path.abspath(self.params['path'])
            directory = os.path.dirname(absolutePath)
            if not os.path.exists(directory):
                os.makedirs(directory)
            self.params['fit'] = self.params['fit'][:1]
            mbr = MBR(size = self.params['size'] * units, fit = self.params['fit'])
            disks[os.path.basename(self.params['path']).split('.')[0]] = {'path': os.path.abspath(self.params['path']), 'ids': {}, 'nextId': 1}
            with open(self.params['path'], 'wb') as file:
                byte = b'\x00'
                for i in range(self.params['size']):
                    file.write(byte * units)
            with open(self.params['path'], 'r+b') as file:
                file.seek(0)
                file.write(mbr.encode())
            return self.__getSuccess(f' -> mkdisk: {os.path.basename(absolutePath).split(".")[0]} creado exitosamente. ({self.params["size"]} {self.params["unit"]}B)')
        else:
            return self.__getError(' -> Error mkdisk: Faltan Parámetros Obligatorios.')

    def __validateParams(self):
        if 'size' in self.params and 'path' in self.params:
            self.params['size'] = int(self.params['size'])
            return True
        return False

    def __getError(self, text):
        return f"{text}"

    def __getSuccess(self, text):
        return f"{text}"

    def __str__(self) -> str:
        return 'Mkdisk'