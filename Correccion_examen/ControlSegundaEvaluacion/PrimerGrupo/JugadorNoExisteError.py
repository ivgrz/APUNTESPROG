class JugadorNoExisteError(Exception):
	"""Excepción que se lanza cuando un jugador no existe"""

	def __init__(self, mensaje):
		self.__mensaje = mensaje

	def __str__(self):
		return "JugadorNoExisteError: " + self.__mensaje

