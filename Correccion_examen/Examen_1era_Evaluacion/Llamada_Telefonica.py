from Cliente import Cliente
import datetime


class Llamada:
    def __init__(self, cliente: Cliente, telefono_i, dhi, dhf, saliente=True):
        self.__cliente = cliente
        self.settelefono_i(telefono_i)
        self.setdhi(dhi)  # Espera "HH:MM:SS"
        self.setdhf(dhf)  # Espera "HH:MM:SS"
        self.setsaliente(saliente)

    # GETTERS
    def get_cliente(self): return self.__cliente

    def gettelefono_i(self): return self.__telefono_i

    def getdhi(self): return self.__dhi

    def getdhf(self): return self.__dhf

    def get_saliente(self): return self.__saliente

    # SETTERS
    def settelefono_i(self, telefono_i):
        if len(telefono_i) == 5:
            self.__telefono_i = telefono_i

    def setdhi(self, dhi):
        self.__dhi = dhi

    def setdhf(self, dhf):
        self.__dhf = dhf

    def setsaliente(self, saliente):
        self.__saliente = saliente

    def duracion(self):
        formato = "%H:%M:%S"
        t_inicio = datetime.datetime.strptime(self.__dhi, formato)
        t_fin = datetime.datetime.strptime(self.__dhf, formato)

        diferencia = t_fin - t_inicio
        # Devolvemos minutos totales
        return diferencia.total_seconds() / 60

    telefono_i = property(gettelefono_i, settelefono_i)
    dhi = property(getdhi, setdhi)
    dhf = property(getdhf, setdhf)
    saliente = property(get_saliente, setsaliente)