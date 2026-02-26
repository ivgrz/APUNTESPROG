# Ejercicio 9: Cifrado César
# Cifrar y descifrar mensajes desplazando letras en el alfabeto


def cifrar(mensaje, desplazamiento):
    """
    Cifra un mensaje desplazando cada letra 'desplazamiento' posiciones.
    Los caracteres que no son letras (espacios, numeros, signos) se quedan igual.
    """
    resultado = ""

    for caracter in mensaje:
        if caracter.isalpha():
            # ord() convierte una letra en su numero ASCII
            # 'a' = 97, 'b' = 98, ..., 'z' = 122
            # 'A' = 65, 'B' = 66, ..., 'Z' = 90

            # Elegimos la base segun sea mayuscula o minuscula
            base = ord('A') if caracter.isupper() else ord('a')

            # 1) ord(caracter) - base  → posicion de 0 a 25 (ej: 'a'=0, 'b'=1, ..., 'z'=25)
            # 2) + desplazamiento      → sumamos el desplazamiento
            # 3) % 26                  → si pasa de 25, vuelve al inicio (esto es lo "circular")
            # 4) + base               → volvemos al codigo ASCII real
            posicion = (ord(caracter) - base + desplazamiento) % 26
            resultado += chr(posicion + base)
        else:
            # Si no es letra (espacio, numero, signo de puntuacion...) se queda igual
            resultado += caracter

    return resultado


def descifrar(mensaje, desplazamiento):
    """
    Descifrar es lo mismo que cifrar pero con el desplazamiento negativo.
    Si cifraste con +3, descifras con -3.
    """
    return cifrar(mensaje, -desplazamiento)


def pedir_entero(texto):
    """Pide un numero entero al usuario, repitiendo si no es valido."""
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Error: introduce un numero entero valido.")


def menu():
    while True:
        print("\n===== CIFRADO CÉSAR =====")
        print("1) Cifrar mensaje")
        print("2) Descifrar mensaje")
        print("3) Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            mensaje = input("Introduce el mensaje a cifrar: ")
            desplazamiento = pedir_entero("Introduce el desplazamiento: ")
            print(f"Mensaje cifrado: {cifrar(mensaje, desplazamiento)}")

        elif opcion == "2":
            mensaje = input("Introduce el mensaje a descifrar: ")
            desplazamiento = pedir_entero("Introduce el desplazamiento usado: ")
            print(f"Mensaje descifrado: {descifrar(mensaje, desplazamiento)}")

        elif opcion == "3":
            print("Hasta luego!")
            break

        else:
            print("Opcion no valida. Elige 1, 2 o 3.")


if __name__ == "__main__":
    menu()
