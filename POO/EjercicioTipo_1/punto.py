class Punto:
	def __init__(self,x,y):
		self.x = x
		self.y = y


	def toString(self):
		cadenapunto = f"Las coordenadas del punto son \n ({self.x}, {self.y})"
		return cadenapunto

	def __str__(self):
		return self.toString()

	def __eq__(self, otro):
		return self.x == otro.x and self.y == otro.y