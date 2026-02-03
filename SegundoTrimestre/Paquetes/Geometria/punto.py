class Punto:
	def __init__(self,x,y):
		self.x = abs(x)
		self.y = abs(y)

	def toString(self):
		cadenapunto = f"El centro de la figura esta en ({self.x}, {self.y})"
		return cadenapunto

	def __str__(self):
		return self.toString()

	def __eq__(self, otro):
		return self.x == otro.x and self.y == otro.y