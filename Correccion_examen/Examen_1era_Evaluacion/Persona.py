class Persona:
    def __init__(self, nombre, dni, cod_postal):
        self.setnombre(nombre)
        self.setdni(dni)
        self.setcod_postal(cod_postal)

    # GETTERS
    def getnombre(self):
        return self.__nombre
    def getdni(self):
        return self.__dni
    def getcod_postal(self):
        return self.__cod_postal

    # SETTERS
    def setnombre(self, nombre):
        self.__nombre = nombre
    def setdni(self, dni):
        self.__dni = dni
    def setcod_postal(self, cod_postal):
        if len(cod_postal) == 5:
            self.__cod_postal = cod_postal
        else:
            print("Error: El código postal está compuesto de 5 dígitos")

    def __eq__(self, otro_dni):
        return self.getdni() == otro_dni

    def __str__(self):
        return (f"Registro de persona con dni {self.getdni()}\n"
                f"Nombre: {self.getnombre()}\n"
                f"Codigo postal: {self.getcod_postal()}\n")

    nombre = property(getnombre, setnombre)
    dni = property(getdni, setdni)
    cod_postal = property(getcod_postal, setcod_postal)