from Fecha import Fecha

class Persona:
	def __init__(self, nombre, edad, dni, direccion, nacionalidad, fecha_nacimiento: Fecha):
		self.nombre = nombre

		if self.comprobaredad(edad):
			self.edad = edad
		else:
			self.edad = 0
		if self.comprobardni(dni):
			self.dni = dni
		else:
			self.dni = "00000000X"
		self.direccion = direccion
		self.nacionalidad = nacionalidad

		self.fecha_nacimiento = fecha_nacimiento

	def comprobaredad(self, edad):
			if isinstance(edad, int) and edad >= 0 and edad <= 150:
				return True
			else:
				return False

	def comprobardni(self, dni):

		if len(dni) == 9 and  dni[:-1].isdigit() and dni[-1:].isalpha():
					letraDni = 'TRWAGMYFPDXBNJZSQVHLCKE'
					resto = int(dni[:-1]) % 23
					if letraDni[resto] == dni[-1].upper():
						return True
					else:
						return False
		else:
			return False
	def __str__(self):
		cadena = f"Nombre: {self.nombre}\n Dni: {self.dni}\n direccion: {self.direccion}\n Nacionalidad: {self.nacionalidad}\n {self.fecha_nacimiento}"

		return cadena

	def __eq__(self, otrap):

		return self.dni == otrap.dni
	def __gt__(self, otrap):
		return self.edad > otrap.edad

	def __lt__(self, otrap):
		return self.edad < otrap.edad

