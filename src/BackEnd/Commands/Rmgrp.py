from Env.Env import *

class Rmgrp:
    def setParams(self, params: dict):
        self.params = params

    def exec(self):
        if currentLogged['User']:
            if currentLogged['User'].name == 'root':
                pass
            else:
                return self.__getError(f" -> Error rmgrp: Solo el usuario 'root' puede eliminar grupos.")
        else:
            return self.__getError(f" -> Error rmgrp: No hay ningún usuario loggeado actualmente.")

    def __getError(self, text):
        return f"{text}"

    def __getSuccess(self, text):
        return f"{text}"