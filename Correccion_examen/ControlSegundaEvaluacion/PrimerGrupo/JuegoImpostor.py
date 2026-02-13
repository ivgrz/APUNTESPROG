from jugador import jugadori
from Partida import Partida


class JuegoImpostor:
    def __init__(self):
        numJugadores = int(input("Cuantos jugadores van a jugar?: "))
        self.__partida = Partida(numJugadores)
        self.iniciarJuego(numJugadores)
        ganador = self.FaseJuego()
        self.FaseFinal(ganador)

    def iniciarJuego(self, numJugadores):

        for i in range(numJugadores):
            nombreJugador = input(
                f"Escribe el nombre del jugador {i+1}/{numJugadores}: ")
            j = jugadori(nombreJugador)
            if self.__partida.add_jugador(j) == -1:
                print("No se pudo añadir el jugador, se alcanzo el maximo.")
                break

        print(
            f"\nSe registraron {numJugadores} jugadores. Comienza la fase de juego!\n")

    def FaseJuego(self):
        nombreJugador = None
        while (True):
            nombreJugador = input(
                "Escribe el nombre del jugador que anoto puntos: ")
            jugador = self.__partida.get_jugador(nombreJugador)
            if jugador is None:
                print(
                    f"No existe un jugador con el nombre '{nombreJugador}'. Intenta de nuevo.")
                continue
            puntos = input(f"Cuantos puntos hizo {jugador}: ")
            jugador.sumar_puntos(int(puntos))
            if jugador.puntuacion >= 50:
                return nombreJugador

    def FaseFinal(self, ganador):
        for jugador in self.__partida.get_jugadores():
            print(
                f"El jugador {jugador.nombre} tiene {jugador.puntuacion} puntos")
        print(f"El jugador ganador es {ganador} !!!  ")
        print("Fin del juego")

    def juego_por_consola(self,):
        self.iniciarJuego(Partida.get_jugadores)
        nombreGanador = self.FaseJuego()
        self.FaseFinal(nombreGanador)

    def juego_por_fichero(self, ruta):
        ruta = open('doc.txt', 'r')
        for linea in ruta:
            print(linea)
        ruta.close()


if __name__ == "__main__":
    juego = JuegoImpostor()
