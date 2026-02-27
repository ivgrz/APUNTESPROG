class persona:
    def __init__(self, nombre, dni, edad, direccion, telefono):
        self.set_nombre(nombre)
        self.set_dni(dni)
        self.set_edad(edad)
        self.set_direccion(direccion)
        self.set_telefono(telefono)



    def get_nombre(self):
        return self.__nombre
    def get_dni(self):
        return self.__dni
    def get_edad(self):
        return self.__edad
    def get_direccion(self):
        return self.__direccion
    def get_telefono(self):
        return self.__telefono

    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_dni(self,dni):
        self.__dni = dni
    def set_edad(self, edad):
        self.__edad = edad
    def set_direccion(self, direccion):
        self.__direccion = direccion
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def comprobar_telefono(self, telefono):

        if telefono.isdigit():
            # Formateo visual: +34 625 844 235
            self.__telefono = "+" + telefono[0:2] + " " + telefono[2:5] + " " + telefono[5:8] + " " + telefono[8:]
        else:
            self.__telefono = "+00 000 000 000"
            print(f"Formato no válido, telefono reestablecido a {self.__telefono}")



    def __eq__(self, otrap):
        return self.dni == otrap.dni




    nombre = property(get_nombre,set_nombre)
    dni = property(get_dni,set_dni)
    edad = property(get_edad,set_edad)
    direccion = property(get_direccion,set_direccion)
    telefono = property(get_telefono,set_telefono)

