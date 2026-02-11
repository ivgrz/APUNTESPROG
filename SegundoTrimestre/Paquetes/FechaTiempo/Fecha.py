import time
import datetime
import re

class Fecha:
	def __init__(self,d, *mesanho):
		self.__dia = 1
		self.__mes = 1
		self.__anho = 1



		match(d):
			case int():

				if len(mesanho) == 2:
					mes, anho = mesanho
					self.anho = anho
					self.mes = mes
					self.dia = d
					print("Fecha creada con día, mes y año.")
				else:
					self.dia = d

			case str():
				partes = re.split(r"[-/]", d)
				if len(partes) == 3:
					self.anho = int(partes[2])
					self.mes = int(partes[1])
					self.dia = int(partes[0])
					print("Fecha creada por texto")
			case list()|tuple():
				if len(d) == 3:
					self.dia = d[0]
					self.mes = d[1]
					self.anho = d[2]
				else:
					raise Exception(f"Error: no hay suficientes elementos")
			case dict():
			# .Subset(d.keys()) funciona para comprobar si un conjunto está contenido en otro, en este caso las claves del diccionario
				if {"dia","mes","anho"}.issubset(d.keys()):
					self.dia = d["dia"]
					self.mes = d["mes"]
					self.anho = d["anho"]
				else:
					raise Exception(f"Error: No se han proporcionado todas las claves necesarias")
			case _:
				raise Exception(f"Error: Tipo de dato no soportado para inicializar Fecha")

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


	# Métodos tradicionales get/set (encapsulación clásica)
	def get_dia(self):
		"""Devuelve el día."""
		return self.__dia

	def set_dia(self, dia_n):
		"""Asigna el día usando validación completa de fecha."""
		# validar con mes y año actuales
		if self._validar_fecha(dia_n, self.__mes, self.__anho):
			self.__dia = dia_n
		else:
			print(f"Asignación de dia rechazada: {dia_n}")

	def get_mes(self):
		"""Devuelve el mes."""
		return self.__mes

	def set_mes(self, mes_nuevo):
		"""Asigna el mes usando validación completa de fecha (considera el dia y año actuales)."""
		if self._validar_fecha(self.__dia, mes_nuevo, self.__anho):
			self.__mes = mes_nuevo
		else:
			print(f"Asignación de mes rechazada: {mes_nuevo}")

	def get_anho(self):
		"""Devuelve el año."""
		return self.__anho

	def set_anho(self, anho_nuevo):
		"""Asigna el año usando validación completa de fecha (considera el dia y mes actuales)."""
		if self._validar_fecha(self.__dia, self.__mes, anho_nuevo):
			self.__anho = anho_nuevo
		else:
			print(f"Asignación de año rechazada: {anho_nuevo}")

	# Encapsulación con propiedad tradicional: nombre = property(get, set)
	# Esto permite el acceso clásico obj.dia y obj.dia = x, pero también deja disponibles
	# los métodos get_*/set_* si se desean usar explícitamente.
	dia = property(get_dia, set_dia)
	mes = property(get_mes, set_mes)
	anho = property(get_anho, set_anho)



	def __str__(self):
		estado_es_bisiesto = "SI" if self._es_bisiesto(self.anho) else "NO"
		return (f"\n Fecha de nacimiento: {self.__dia}/{self.__mes}/{self.__anho}\n"
				f"Este año {self.__anho} {estado_es_bisiesto} fue bisiesto")
