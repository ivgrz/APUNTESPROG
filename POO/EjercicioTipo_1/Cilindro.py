import math

from TiposBasicos import cadena
from punto import Punto

class Cilindro(Punto):
	def __init__(self,x,y,radio,altura):
		super().__init__(
			x,y
		)
		self.radio = abs(radio)
		self.altura = abs(altura)

	def CalcularArea(self):
		return 2 * math.pi * self.radio * (self.radio + self.altura)
	def CalcularVolumen(self):
		return math.pi * (self.radio ** 2) * self.altura

	def Cadena(self):
		cadena = (
			f"{super().toString()}\n"
			f"\n CREAMOS CILINDRO\n"
			f"Radio: {self.radio:.2f}, Altura: {self.altura:.2f} "
			f"Area: {self.CalcularArea():.2f}, Volumen: {self.CalcularVolumen():.2f}"
		)
		return cadena

