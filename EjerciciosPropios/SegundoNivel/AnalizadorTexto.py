def analizador_texto():
    oracion = input("Añade una oracion: ")

    palabra = oracion.split()
    cantidad_palabras = len(palabra)
    contador_letras = 0
    contador_vocales = 0
    vocales = "AEIOUaeiou"

    print(f"Hay {cantidad_palabras} palabras")
    for i in oracion:
        if i != " ":
            contador_letras += 1
        if i in vocales:
            contador_vocales += 1

    print(f"{contador_letras} letras")
    print(f"{contador_vocales} vocales")


if __name__ == "__main__":
    analizador_texto()
