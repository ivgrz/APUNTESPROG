from Dnierror import Dnierror
from nussError import nussError
class Persona2:
	def __init__(self,nombre,edad,dni, nuss):
		self.set_nombre(nombre)
		self.set_edad(edad)
		self.set_dni(dni)
		self.set_nuss(nuss)

	def get_nombre(self):
		return self.__nombre
	def get_edad(self):
		return self.__edad
	def get_dni(self):
		return self.__dni
	def set_nombre(self, nombre):
		self.__nombre = nombre
	def set_edad(self, edad):
		if isinstance(edad, int):
			if edad >= 0:
				self.__edad = edad
			else:
				raise TypeError(f"La edad debe ser positiva")
		else:
			raise TypeError(f"La edad debe ser un entero no {type(edad)}")
	def set_dni(self, dni):
		if dni is None:
			self.__dni = None
			return
		Dnierror.validar(dni)
		self.__dni = dni
	def get_nuss(self):
		return self.__nuss
	def set_nuss(self, nuss):
		if nuss is None:
			raise nussError(f"El nuss no puede estar vacio", nuss)
			return
		nussError.validar(nuss)
		self.__nuss = nuss.strip()

	def __str__(self):
		return (
				f"Nombre: {self.get_nombre()}\n"
				f"Edad: {self.get_edad()}\n"
				f"DNI: {self.get_dni()}\n"
				f"NUSS: {self.get_nuss()}")



	nombre = property(get_nombre,set_nombre)
	edad = property(get_edad,set_edad)
	dni = property(get_dni,set_dni)
	nuss = property(get_nuss,set_nuss)
