import math

from cono import Cono

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

		return (1/3) * math.pi	* h * (R**2 * r**2 + R*r)

	def __str__(self):
		return (f"---- CREAMOS CONO TRUNCADO ----"
				f"{super().toString()}"
				f"Radio mayor : {self.radio}"
				f"Radio menor : {self.rmen}"
				f"Altura: {self.h}"
				f"Area: {self.CalcularAreaTotal()}"
				f"Volumen: {self.calcularVolumen()}")

