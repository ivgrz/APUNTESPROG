"""Ejercicio: Juego del Ahorcado"""

import random
import unicodedata

def normalizar_entrada(cadena):
    # Descompone el carácter base y la tilde (NFD)
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    # Filtra y concatena solo los caracteres que NO son marcas no espaciadoras ('Mn')
    sin_tildes = ''.join(c for c in cadena_normalizada if unicodedata.category(c) != 'Mn')
    return sin_tildes


def jugar_ahorcado():
    # 1. Lista de palabras posibles
    palabras = ['python', 'programacion', 'computadora', 'desarrollo', 'codigo', 'algoritmo']

    # 2. Elegir una palabra al azar
    # Mantenemos las palabras sin tildes en la lista para simplificar la lógica del juego.
    # Si la lista tuviera palabras con tildes (ej: 'algorítmo'), la palabra_secreta también debería
    # ser normalizada y sin tildes para que el juego funcione correctamente.
    palabra_secreta = random.choice(palabras).upper()  # Convertir a mayúsculas

    # 3. Inicializar variables del juego
    letras_adivinadas = set()
    letras_falladas = set()
    intentos_maximos = 6
    intentos_restantes = intentos_maximos

    print("¡Bienvenido al juego del Ahorcado! 🔪")
    print(f"Tienes {intentos_maximos} intentos para adivinar la palabra.")

    # Bucle principal del juego
    while intentos_restantes > 0:

        # 4. Mostrar el estado de la palabra (código sin cambios)
        estado_palabra = ""
        palabra_completa = True
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                estado_palabra += letra + " "
            else:
                estado_palabra += "_ "
                palabra_completa = False

        print("\nPalabra: ", estado_palabra)
        print("Intentos restantes:", intentos_restantes)
        print("Letras falladas:", ", ".join(sorted(letras_falladas)))

        # 5. Comprobar si ha ganado (código sin cambios)
        if palabra_completa:
            print(f"\n¡Felicidades! Has adivinado la palabra: **{palabra_secreta}** 🎉")
            break

        # 6. Pedir la letra al jugador (¡AQUÍ ESTÁ EL CAMBIO! 👇)
        while True:
            intento_original = input("Adivina una letra: ").upper()

            # --- Nuevo paso para normalizar la entrada ---
            intento = normalizar_entrada(intento_original)
            # ---------------------------------------------

            # Validar la entrada (ahora se valida 'intento', que ya no tiene tildes)
            if len(intento) != 1 or not intento.isalpha():
                # Si el usuario escribe una letra con tilde (ej: 'Á'), después de normalizar,
                # 'intento' será 'A', y len(intento) será 1.
                # Si escribe algo como 'ñ', después de normalizar, seguirá siendo 'Ñ',
                # y isalpha() lo considerará válido. Si no quieres permitir la 'Ñ', deberías
                # validar también que la letra esté en el abecedario ASCII.
                if len(intento) == 1 and intento.isalpha():
                    # Esto ocurre si el usuario escribe 'Á' o 'Ñ'.
                    # El bucle continúa, intentando la letra ya normalizada.
                    pass
                else:
                    print("Por favor, introduce una única letra válida.")
                    continue  # Vuelve a pedir la letra

            elif intento in letras_adivinadas or intento in letras_falladas:
                print(f"Ya has intentado la letra '{intento_original}' (o su versión sin tilde). Intenta con otra.")
            else:
                break

        # 7. Procesar el intento (código sin cambios, usa 'intento' ya normalizado)
        if intento in palabra_secreta:
            print("¡Acierto! La letra está en la palabra. ✅")
            letras_adivinadas.add(intento)
        else:
            print("¡Fallaste! Esa letra no está. ❌")
            letras_falladas.add(intento)
            intentos_restantes -= 1

    # 8. Comprobar si ha perdido (código sin cambios)
    else:
        print("\n¡Oh no! Te has quedado sin intentos. 💀")
        print(f"La palabra secreta era: **{palabra_secreta}**")

jugar_ahorcado()