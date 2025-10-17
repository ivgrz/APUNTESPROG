"""Ejercicio: Juego del Ahorcado"""
import random


def jugar_ahorcado():
    # 1. Lista de palabras posibles
    palabras = ['python', 'programacion', 'computadora', 'desarrollo', 'codigo', 'algoritmo']

    # 2. Elegir una palabra al azar
    palabra_secreta = random.choice(palabras).upper()  # Convertir a mayúsculas para simplificar

    # 3. Inicializar variables del juego
    letras_adivinadas = set()  # Conjunto para almacenar las letras correctas adivinadas
    letras_falladas = set()  # Conjunto para almacenar las letras incorrectas adivinadas
    intentos_maximos = 6
    intentos_restantes = intentos_maximos

    print("¡Bienvenido al juego del Ahorcado! 🔪")
    print(f"Tienes {intentos_maximos} intentos para adivinar la palabra.")

    # Bucle principal del juego
    while intentos_restantes > 0:

        # 4. Mostrar el estado de la palabra
        estado_palabra = ""
        palabra_completa = True
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                estado_palabra += letra + " "
            else:
                estado_palabra += "_ "
                palabra_completa = False  # La palabra aún no está completa

        print("\nPalabra: ", estado_palabra)
        print("Intentos restantes:", intentos_restantes)
        print("Letras falladas:", ", ".join(sorted(letras_falladas)))

        # 5. Comprobar si ha ganado
        if palabra_completa:
            print(f"\n¡Felicidades! Has adivinado la palabra: **{palabra_secreta}** 🎉")
            break

        # 6. Pedir la letra al jugador
        while True:
            intento = input("Adivina una letra: ").upper()

            # Validar la entrada
            if len(intento) != 1 or not intento.isalpha():
                print("Por favor, introduce una única letra válida.")
            elif intento in letras_adivinadas or intento in letras_falladas:
                print(f"Ya has intentado la letra '{intento}'. Intenta con otra.")
            else:
                break  # La entrada es válida, salir del bucle de validación

        # 7. Procesar el intento
        if intento in palabra_secreta:
            print("¡Acierto! La letra está en la palabra. ✅")
            letras_adivinadas.add(intento)
        else:
            print("¡Fallaste! Esa letra no está. ❌")
            letras_falladas.add(intento)
            intentos_restantes -= 1  # Reducir los intentos

    # 8. Comprobar si ha perdido
    else:  # El bucle while terminó porque intentos_restantes llegó a 0
        print("\n¡Oh no! Te has quedado sin intentos. 💀")
        print(f"La palabra secreta era: **{palabra_secreta}**")


# Ejecutar el juego
if __name__ == "__main__":
    jugar_ahorcado()