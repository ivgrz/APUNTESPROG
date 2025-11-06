class Punto:
	def __init__(self,x,y):
		self.x = x
		self.y = y


	def toString(self):
		cadenaPunto = f"Las coordenadas del punto son \n ({self.x}, {self.y})"
		return cadenaPunto

	def __str__(self):
		return self.toString()