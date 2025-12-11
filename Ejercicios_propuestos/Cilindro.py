import math

from TiposBasicos import cadena
from punto import Punto
from POO.EjercicioTipo_1.circulo import Circulo

class Cilindro(Circulo):
	def __init__(self,x=0.0,y=0.0,radio=1.0,altura=1.0):
		super().__init__(x,y,radio)
		self.altura = abs(altura)

	def CalcularArea(self):
		return 2 * math.pi * self.radio * (self.radio + self.altura)
	def CalcularVolumen(self):
		return super().CalcularArea() * self.altura

	def Cadena(self):
		cadena = ( f"\n CREAMOS CILINDRO\n"
			f"{super().toString()}\n"
			
			f"Radio: {self.radio:.2f}, Altura: {self.altura:.2f} "
			f"Area: {self.CalcularArea():.2f}, Volumen: {self.CalcularVolumen():.2f}"
		)
		return cadena

	def __str__(self):
		return self.Cadena()

