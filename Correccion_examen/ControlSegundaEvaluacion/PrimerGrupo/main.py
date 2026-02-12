from Partida import Partida
from jugador import jugadori
if __name__ == '__main__':
	x1 = jugadori("Pepe",30,25)
	x2 = jugadori("Ana",35,28)
	x3 = jugadori("Xoan",40,33)
	x4 = jugadori("Mario",14,22)

	p1 = Partida(4)

	p1.add_jugador(x1)
	p1.add_jugador(x2)
	p1.add_jugador(x3)
	p1.add_jugador(x4)

	p1.get_jugador_con_min_puntos(15)



