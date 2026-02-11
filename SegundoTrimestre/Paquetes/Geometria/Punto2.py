class Punto2:
	def __init__(self,x,y):
		# Inicializamos los atributos privados antes de usar los setters
		self.__x = 0
		self.__y = 0
		# Usamos los setters para validación
		self.setx(x)
		self.sety(y)

	def setx(self,x):
		if type(x) == int or type(x) == float:

			if	x >= 0:
					self.__x = x
			else:
					print(f"Error: Solo valores positivos")
		else:

			print(f"Error: Haz introducido un valor de tipo {type(x).__name__} y solo se admiten valores positivos")
			print(
					f"Se procederá a restablecer la figura en el origen (0,0).")
			self.__x = 0
			self.__y = 0
			print(f"Coordenadas restablecidas: ({self.__x},{self.__y})")


	def sety(self,y):
		if type(y) == int or type(y) == float:

			if y >= 0:
				self.__y = y
			else:
				print(f"Error: Solo valores positivos")
		else:

			print(f"Error: Solo valores positivos")
			print(
				f"Se procederá a restablecer la figura en el origen (0,0).")
			self.__x = 0  # <--- Asignación a 0
			self.__y = 0  # <--- Asignación a 0
			print(f"Coordenadas restablecidas: ({self.__x},{self.__y})")



	def getx(self):
		return self.__x
	def gety(self):
		return self.__y




	def __eq__(self, otro):
		return self.__x == otro.x and self.__y == otro.y


	def __str__(self):
		return f"El centro de la figura esta en ({self.__x},{self.__y})"

	x = property(getx,setx)
	y = property(gety,sety)