from Env.Env import *
import os

class Rmdisk:
    def __init__(self, path : str = None):
        self.path = path.replace('"', '')

    def exec(self):
        if not self.path:
            return self.__getError(' -> Error rmdisk: No se especificó el disoc que quiere eliminar.')
        absolutePath = os.path.abspath(self.path)
        if not os.path.exists(absolutePath):
            return self.__getError(' -> Error rmdisk: No existe el disco que quiere eliminar.')
        del disks[os.path.basename(absolutePath).split('.')[0]]
        os.remove(self.path)
        return self.__getSuccess(f' -> rmdisk: Disco {os.path.basename(absolutePath).split(".")[0]} elminado exitosamente.')

    def __getError(self, text):
        return f"{text}"

    def __getSuccess(self, text):
        return f"{text}"