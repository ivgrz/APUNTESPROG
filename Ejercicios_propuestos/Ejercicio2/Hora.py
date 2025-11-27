class Hora:

	def __init__(self, hora: int, minuto: int, segundo: int):
		self.__hora = hora
		self.__minuto = minuto
		self.__segundo = segundo


	# GETTERS

	def get_hora(self) -> int:
		return self.__hora
	def get_minuto(self) -> int:
		return self.__minuto
	def get_segundo(self) -> int:
		return self.__segundo

	# SETTERS

	def set_hora(self, hora: int):
		self.__hora = hora % 24
	def set_minuto(self, minuto: int):
		self.__minuto = minuto % 60
	def set_segundo(self, segundo: int):
		self.__segundo = segundo % 60

	# METODOS

	def convertir_minutos(self, minutos):

		if minutos >= 60:
			self.__hora += 1
			minutos -= 60
		else:
			self.__minuto = minutos

		return self.__hora , self.__minuto

	def convertir_segundos(self, segundos):

		if segundos >= 60:
			self.__minuto += 1
			segundos -= 60
		else:
			self.__segundo = segundos

		return self.__minuto, self.__segundo

	def incrementar_minutos(self, minutos):

		n_minutos = self.__minuto + minutos

		return n_minutos

	def incrementar_segundos(self, segundos):

		n_segundos = self.__segundo + segundos

		return n_segundos

	def incrementar_horas(self, horas):

		n_horas = self.__hora + horas

		return n_horas

	# Mostrar formato 12 horas

	def __str__(self):


		return (
			f"=== Horas ==="
			f"La hora original es {self.__hora}:{self.__minuto}:{self.__segundo}"
			f""
		)
