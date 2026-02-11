import math

from .cono import Cono

class Cono_truncado(Cono):
	def __init__(self,x,y,rm,h,rmen):
		super().__init__(x,y,rm,h)
		self.rmen = abs(rmen)

	def calcularArea(self):
		R = self.radio
		r = self.rmen
		h = self.h

		generatriz = math.sqrt(h**2 + (R - r)**2)
		area_lateral =math.pi * (R + r) * generatriz
		area_base_mayor = math.pi * R**2
		area_base_menor = math.pi * r**2

		return area_base_mayor + area_base_menor + area_lateral

	def calcularVolumen(self):
		R = self.radio
		r = self.rmen
		h = self.h

		# Fórmula correcta del volumen del tronco de cono: (1/3) * pi * h * (R^2 + R*r + r^2)
		return (1/3) * math.pi * h * (R**2 + R*r + r**2)

	def __str__(self):
		return (f"---- CREAMOS CONO TRUNCADO ----\n"
				f"{super().toString()}\n"
				f"Radio mayor : {self.radio}\n"
				f"Radio menor : {self.rmen}\n"
				f"Altura: {self.h}\n"
				f"Area: {self.calcularArea()}\n"
				f"Volumen: {self.calcularVolumen()}")
