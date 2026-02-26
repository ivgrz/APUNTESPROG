import random


def adivinar_numero():
    numero_secreto = random.randint(1, 20)
    contador = 0
    intentos = 7

    while True:
        print("Adivina el numero -_- ")
        opcion = int(input(": "))
        contador += 1

        if contador == 7:
            print("Te quedaste sin intentos :c")

            break
        elif opcion == numero_secreto:
            print(f"Adivinaste!! El numero era {numero_secreto}")
        else:
            intentos -= 1
            print(f"Casi, te quedan {intentos} intentos")

            continue


if __name__ == "__main__":
    adivinar_numero()
