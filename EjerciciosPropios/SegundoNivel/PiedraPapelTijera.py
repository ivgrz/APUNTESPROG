import random


def piedra_papel_tijera():
    eleccion = ['piedra', 'papel', 'tijera']
    nombre = input("Ingresa tu nombre: ")
    while True:
        eleccion_maquina = random.choice(eleccion)

        eleccion_usuario = input("Elige Piedra Papel o Tijera: ")
        eleccion_usuario = eleccion_usuario.lower()
        if eleccion_usuario == "salir":
            break
        else:
            print(f"Maquina elige: {eleccion_maquina}")
            if eleccion_usuario == eleccion_maquina:
                print("EMPATE")
            elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera"
                  or eleccion_usuario == "papel" and eleccion_maquina == "piedra"
                  or eleccion_usuario == "tijera" and eleccion_maquina == "papel"):
                print(f"Gana {nombre}")
            else:
                print("Gana la maquina")


if __name__ == "__main__":
    piedra_papel_tijera()
