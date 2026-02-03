import math

from circulo import Circulo

class Esfera(Circulo):
	def __init__(self, x=0.0, y=0.0, radio=1.0):
		super().__init__(x,y,radio)

	def calcularAreaEsfera(self):
		return super().CalcularArea() * 4

	def calcularVolumen(self):

		return (4/3) * math.pi * (self.radio ** 3)

	def Cadena(self):
		Cadena = (
			f"\n------ CREACION DE ESFERA -------\n"
			f"{super().toString()}\n"
			f"El radio de la esfera es de {self.radio:.2f}\n"
			f"El area de esta esfera es de {self.CalcularArea():.2f}\n"
			f"El volumen de esta esfera es de {self.calcularVolumen():.2f}"
		)

		return Cadena

	def __str__(self):
		return self.Cadena()