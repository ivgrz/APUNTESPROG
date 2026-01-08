from logging import exception


class CalculadoraBinaria:

	def __init__(self, a,b):
		self.set_a(a)
		self.set_b(b)


	def get_a(self):
		return self.__a
	def get_b(self):
		return  self.__b
	def set_a(self,a):
		if isinstance(a, int) or isinstance(a, float):
			self.__a = a
		else:
			raise ValueError(f"Caracter {a} no valido")
	def set_b(self,b):
		if isinstance(b, int) or isinstance(b, float):
			self.__b = b
		else:
			raise ValueError(f"Caracter {b} no valido")


	def operacion(self,opcion):

		if opcion == 1:
			resultado = self.get_a() + self.get_b()
		elif opcion == 2:
			resultado = self.get_a() - self.get_b()
		elif opcion == 3:
			resultado = self.get_a() * self.get_b()
		elif opcion == 4:
			resultado = self.get_a() / self.get_b()
		else:
			raise ValueError("Operacion no valida")

		return resultado

	a = property(get_a,set_a)
	b = property(get_b,set_b)



