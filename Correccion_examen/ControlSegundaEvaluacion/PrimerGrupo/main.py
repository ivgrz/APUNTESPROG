from Partida import Partida
from jugador import jugadori
if __name__ == '__main__':
	x1 = jugadori("Pepe")
	x2 = jugadori("Ana")
	x3 = jugadori("Xoan")
	x4 = jugadori("Mario")

	p1 = Partida(4)

	p1.add_jugador(x1)