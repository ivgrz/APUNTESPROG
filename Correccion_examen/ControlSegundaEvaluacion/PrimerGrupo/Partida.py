from jugador import jugadori
class Partida:
	def __init__(self, num_jugadores):
		self.__jugadores = []
		self._num_max_jugadores = num_jugadores

	def add_jugador(self, jugador:jugadori):

		if isinstance(jugador, object):
			self.__jugadores.append(jugador)
		else:
			raise ValueError("Formato invalido")

	def get_jugador(self, nombre):

		for jugador in self.__jugadores:
			if jugador.nombre == nombre:
				return self.__jugadores[jugador]
		return None



