import math

from punto import Punto

class Circulo (Punto):
	def __init__(self,x,y, radio):
		super().__init__(
			x,  y
		)
		self.radio = abs(radio)

	def ObtenerDiametro(self):

		return 2 * self.radio

	def ObtenerPerimetro(self):

		"""Devuelve el diametro del circulo"""



		return  2 * self.radio * math.pi


	def CalcularArea(self):
		"""Devuelve el area del circulo"""



		return (math.pi) * self.radio ** 2

	def Cadena(self):
		cadena = (f"{super().toString()}\n"
				  f"\nCREAMOS CIRCULO\n"
				  f"Radio: {self.radio:.2f}\n"
				f"Diametro: {self.ObtenerDiametro()}\n"
				f"Area: {self.CalcularArea():.2f}\n"
				f"Perimetro: {self.ObtenerPerimetro():.2f}")

		return cadena
