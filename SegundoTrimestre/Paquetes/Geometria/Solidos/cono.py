import math
from ..circulo import Circulo


class Cono(Circulo):
	def __init__(self,x = 0.0, y = 0.0, radio = 1.0, h = 0.0):
		super().__init__(x,y,radio)
		self.h = abs(h)

	def CalcularAreaTotal(self):
		generatriz = math.sqrt(self.radio ** 2 + self.h ** 2)
		area_lateral = math.pi * self.radio *  generatriz
		area_base = super().CalcularArea()

		return area_lateral + area_base

	def VolumenCono(self):
		area_base = super().CalcularArea()

		return (1/3) * area_base * self.h

	def __str__(self):
		return (
			f"\n----- CREANDO CONO -----\n"
			f"{super().toString()}\n"
			f"El radio del cono es de {self.radio} metros\n"
			f"La altura del cono es  de {self.h} metros\n"
			f"El area del cono es {self.CalcularArea():.2f}\n"
			f"El volumen del cono es {self.VolumenCono():.2f}\n"
		)