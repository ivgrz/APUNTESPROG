class jugadori:
	def __init__(self, nombre="", puntuacion=0, edad=0):
		self.nombre = nombre
		self.puntuacion = puntuacion
		self.edad = edad

	@property
	def nombre(self):
		return self.__nombre
	@nombre.setter
	def nombre(self, nombre):
		if isinstance(nombre, str):
			self.__nombre = nombre
		else:
			self.__nombre = ""
	@property
	def puntuacion(self):
		return self.__puntuacion
	@puntuacion.setter
	def puntuacion(self, puntuacion):
		if isinstance(puntuacion, int):
			self.__puntuacion = puntuacion
		else:
			self.__puntuacion = 0
	@property
	def edad(self):
		return self.__edad
	@edad.setter
	def edad(self, edad):
		if isinstance(edad, int):
			self.__edad = edad
		else:
			self.__edad = 0




