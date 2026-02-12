from jugador import jugadori
class Partida:
	def __init__(self, num_jugadores):
		self.__jugadores = []
		self._num_max_jugadores = num_jugadores

	def add_jugador(self, jugador:jugadori):

		if isinstance(jugador, object) | len(self.__jugadores) < self._num_max_jugadores:
			self.__jugadores.append(jugador)
			return len(self.__jugadores)-1
		else:
			return -1

	def get_jugador(self, nombre):

		for jugador in self.__jugadores:
			if jugador.nombre == nombre:
				return self.__jugadores[jugador]
		return None

	def get_jugadores(self):
		return self.__jugadores

	def get_jugador_con_min_puntos(self, puntos):
		for jugador in self.__jugadores:
			if jugador.puntuacion() >= puntos:
				return jugador
		return -1

	def add_puntos_a_jugador(self, nombre_puntos):
		"""formato de nombre_puntos: 'nome_xogador puntos'"""
		f_nombre_puntos = nombre_puntos.strip()
		nombre, puntuacion = f_nombre_puntos
		n_s = nombre
		p_s = puntuacion
		jugador = self.get_jugador(n_s)
		if jugador:
			jugador.sumar_puntos(p_s)







