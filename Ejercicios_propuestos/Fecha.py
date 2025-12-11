import math
class Fecha:





	def __init__(self,dia,mes,anho):

		self.__mes = 1
		self.__dia = 1
		self.__anho = 1900

		self.mes = mes
		self.dia = dia
		self.anho = anho


	def _es_bisiesto(self, anho):
		return (anho % 4 == 0 and anho % 100 != 0) or (anho % 400 == 0)


	def _validar_fecha(self, dia_n, mes_n, anho_n):
		if not isinstance(anho_n, int) or anho_n <= 0:
			print(f"Error: El año {anho_n} no es entero.")
			return False
		if not isinstance(mes_n, int) or not  (12 >= mes_n >= 1):
			print(f"Error: El mes {mes_n} no es valido")
			return False
		if not isinstance(dia_n, int) or not (31 >= dia_n >= 1):
			print(f"Error: El dia {dia_n} no es valido")
			return False
		dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		limite_dia = dias_por_mes[mes_n]
		if mes_n == 2 and self._es_bisiesto(anho_n):
			limite_dia = 29

		if dia_n > limite_dia:
			print(f"Error: El dia {dia_n} es mayor de lo permitido para el mes {mes_n}")
			return False
		return True


	"""
	GETTERS
	"""
	@property
	def dia(self):
		return self.__dia
	@property
	def mes(self):
		return self.__mes
	@property
	def anho(self):
		return self.__anho
	"""
	SETTERS
	"""
	@dia.setter
	def dia(self,dia_n):
		if 1 <= dia_n <= 31:
			self.__dia = dia_n
		else:
			print(f"El dia {dia_n} no es valido. No se aceptan mas de 31 dias")
	@mes.setter
	def mes(self,mes_nuevo):
		if self._validar_fecha(self.__dia,self.__mes,self.__anho):
			self.__mes = mes_nuevo
			if not self._validar_fecha(self.__dia,self.__mes,self.__anho):
				print(f"Cuidado: El dia {self.__dia} es demasiado alto para el mes{self.__mes}")
				self.__dia = 1

		else:
			print(f"Asignacion rechazada :c")
	@anho.setter
	def anho(self,anho_nuevo):
		if self._validar_fecha(self.__dia,self.__mes,self.__anho):
			self.__anho = anho_nuevo
			if not self._validar_fecha(self.__dia,self.__mes,self.__anho):
				print(f"Cuidado: El dia {self.__dia} no es valido para el año {self.__anho}")
				self.__dia = 1
		else:
			print(f"Asignacion rechazada")

	def __str__(self):
		estado_es_bisiesto = "SI" if self._es_bisiesto(self.anho) else "NO"
		return (f"\n Fecha de nacimiento: {self.__dia}/{self.__mes}/{self.__anho}\n"
				f"Este año {self.__anho} {estado_es_bisiesto} fue bisiesto")







