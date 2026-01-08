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



	def convertir_segundos(self):

		if self.__segundo >= 60:
			acarreo_minutos = self.__segundo // 60
			self.__segundo %= 60
			self.__minuto += acarreo_minutos
	def convertir_minutos(self):
		if self.__minuto >= 60:

			acarreo_horas = self.__minuto // 60
			self.__minuto %= 60
			self.__hora = (self.__hora + acarreo_horas) % 24






	def incrementar_minutos(self, minutos):

		self.__minuto += minutos
		self.convertir_minutos()
		return self


	def incrementar_segundos(self, segundos):

		self.__segundo += segundos
		self.convertir_segundos()
		return self



	def incrementar_horas(self, horas):

		self.__hora = (self.__hora + horas) % 24

	# Mostrar formato 12 horas
	def mostrar_formato_12horas(self):
		horas_12 = self.__hora % 12
		if horas_12 == 0:
			horas_12 = 12

		am_pm = "AM" if self.__hora < 12 else "PM"
		return (
				f"{horas_12}: {self.__minuto}: {self.__segundo} {am_pm}")

	def __str__(self):


		return (

			self.mostrar_formato_12horas()
		)
