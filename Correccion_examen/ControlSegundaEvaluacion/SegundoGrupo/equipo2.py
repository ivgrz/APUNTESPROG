class Equipo:
    def __init__(self, nome, ganhados=0, perdidos=0, empates=0):
        self.nome = nome
        self.ganhados = ganhados
        self.perdidos = perdidos
        self.empates = empates

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = ""
    @property
    def ganhados(self):
        return self.__ganhados
    @ganhados.setter
    def ganhados(self, ganhados):
        if isinstance(ganhados, int):
            self.__ganhados = ganhados
        else:
            self.__ganhados = 0
    @property
    def perdidos(self):
        return self.__perdidos
    @perdidos.setter
    def perdidos(self, perdidos):
        if isinstance(perdidos, int):
            self.__perdidos = perdidos
        else:
            self.__perdidos = 0
    @property
    def empates(self):
        return self.__empates
    @empates.setter
    def empates(self, empates):
        if isinstance(empates, int):
            self.__empates = empates
        else:
            self.__empates = 0
    def add_victoria(self, victorias):
        if isinstance(victorias, int) | victorias > 0:
            self.ganhados += victorias
        else:
            raise Exception("Los partidos ganados tienen que ser enteros", victorias)
        return self.ganhados

    def add_perdidos(self, perdidos):
        if isinstance(perdidos, int) | perdidos > 0:
            self.perdidos += perdidos

        else:
            raise Exception("Los partidos perdidos tienen que ser enteros", perdidos)
        return self.perdidos

    def add_empate(self, empates):

        if isinstance(empates, int) | empates > 0:
            self.empates += empates
        else:
            raise Exception("Los partidos empatados tienen que ser enteros", empates)
        return self.empates
    def get_puntos(self):
        puntos_victoria = self.ganhados * 3
        puntos_derrota = self.perdidos * 0
        puntos_empates = self.empates * 1
        puntos_totales = puntos_victoria + puntos_derrota + puntos_empates
        return puntos_totales

    def get_encuentros_jugados(self):
        encuentros_jugados = self.ganhados + self.perdidos + self.empates
        return encuentros_jugados

    def __str__(self):
        return (f"El equipo {self.__nome} ha disputado {self.get_encuentros_jugados()} encuentros con un resultado de: \n"
                f"V: {self.__ganhados}\n"
                f"D: {self.__perdidos}\n"
                f"E: {self.__empates}\n"
                f"Terminando con un total de {self.get_puntos()} puntos")






