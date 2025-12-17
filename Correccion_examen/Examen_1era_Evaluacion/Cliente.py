from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre: str, dni: str, cod_postal, telefono: str):
        # Llamamos al constructor de Persona
        super().__init__(nombre, dni, cod_postal)
        self.settelefono(telefono)

    def gettelefono(self):
        return self.__telefono

    def settelefono(self, telefono):
        # Verificamos si son dígitos (el teléfono debe venir como string)
        if telefono.isdigit():
            # Formateo visual: +34 625 844 235
            self.__telefono = "+" + telefono[0:2] + " " + telefono[2:5] + " " + telefono[5:8] + " " + telefono[8:]
        else:
            self.__telefono = "+00 000 000 000"
            print(f"Formato no válido, telefono reestablecido a {self.__telefono}")

    def __str__(self):
        # Aprovechamos el __str__ de Persona y añadimos el teléfono
        return super().__str__() + f"Telefono: {self.gettelefono()}\n"

    telefono = property(gettelefono, settelefono)