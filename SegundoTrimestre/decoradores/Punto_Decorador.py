class PuntoDecorador:
	def __init__(self, x, y):
		# Inicializamos los atributos privados antes de usar los setters
		self.__x = 0
		self.__y = 0
		# Usamos los setters para validación
		self.x = x
		self.y = y


	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y


	@x.setter
	def x(self, x):

		if isinstance(x, (int, float)):
			if x >= 0:
				self.__x = x
			else:
				raise Exception("Error: Solo valores positivos para x. Se mantiene el valor anterior.")
		else:

			self.__x = 0
			self.__y = 0
			print(f"Coordenadas restablecidas: ({self.__x},{self.__y})")
			raise Exception(
				f"Error: Haz introducido un valor de tipo {type(x).__name__} para x; se restablecerá a (0,0).")

	@y.setter
	def y(self, y):
		if isinstance(y, (int, float)):
			if y >= 0:
				self.__y = y
			else:
				raise Exception("Error: Solo valores positivos para y. Se mantiene el valor anterior.")
		else:

			self.__x = 0
			self.__y = 0
			print(f"Coordenadas restablecidas: ({self.__x},{self.__y})")
			raise Exception(
				f"Error: Haz introducido un valor de tipo {type(y).__name__} para y; se restablecerá a (0,0).")




	def __eq__(self, otro):

		if not isinstance(otro, PuntoDecorador):
			return NotImplemented
		return self.__x == otro.x and self.__y == otro.y


	def __str__(self):
		return f"El centro de la figura está en ({self.__x},{self.__y})"
