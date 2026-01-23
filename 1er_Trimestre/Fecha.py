class Fecha:
	def __init__(self,dia,mes,anho):

		self.set_mes(mes)
		self.set_dia(dia)
		self.set_anho(anho)


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
