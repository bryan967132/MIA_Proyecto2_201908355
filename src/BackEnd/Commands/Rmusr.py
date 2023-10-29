from Env.Env import *

class Rmusr:
    def setParams(self, params: dict):
        self.params = params

    def exec(self):
        if currentLogged['User']:
            if currentLogged['User'].name == 'root':
                pass
            else:
                return self.__getError(f" -> Error rmusr: Solo el usuario 'root' puede eliminar usuarios.")
        else:
            return self.__getError(f" -> Error rmusr: No hay ningún usuario loggeado actualmente.")

    def __getError(self, text):
        return f"{text}"

    def __getSuccess(self, text):
        return f"{text}"