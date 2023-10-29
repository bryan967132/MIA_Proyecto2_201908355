from Structures.SuperBlock import *
from Structures.MBR import *
from Env.Env import *

class Logout:
    def exec(self):
        if currentLogged['User']:
            response = f" -> logout: Sesión finalizada exitosamente. ({currentLogged['User'].name})"
            currentLogged['User'] = None
            currentLogged['Partition'] = None
            currentLogged['PathDisk'] = None
            currentLogged['IDPart'] = None
            return response
        else:
            return f" -> Error logout: No hay ningún usuario loggeado actualmente."