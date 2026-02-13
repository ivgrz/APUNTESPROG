from jugador import jugadori
from Partida import Partida
class JuegoImpostor:
	def __init__(self):
		self.__partida = None
		self.iniciarJuego()
		ganador = self.FaseJuego()
		self.FaseFinal(ganador)

	def iniciarJuego(self):
		numJugadores = int(input("Cuantos jugadores van a jugar?: "))
		self.__partida = Partida(numJugadores)

		for _ in range(numJugadores):
			nombreJugador = input("Escribe el nombre del jugador: ")
			j = jugadori(nombreJugador)
			self.__partida.add_jugador(j)

	def FaseJuego(self):
		nombreJugador = None
		while (True):
			nombreJugador = input("Escribe el nombre del jugador: ")
			jugador = self.__partida.get_jugador(nombreJugador)
			if jugador is not None:
				puntos = input(f"Cuantos puntos hizo {jugador}: ")
				jugador.sumar_puntos(int(puntos))
				if jugador.puntuacion >= 50:
					return nombreJugador


	def FaseFinal(self, ganador):
		for jugador in self.__partida.get_jugadores():
			print(f"El jugador {jugador.nombre} tiene {jugador.puntuacion} puntos")
		print(f"El jugador ganador es {ganador} !!!  ")
		print("Fin del juego")


if __name__ == "__main__":
	juego = JuegoImpostor()



