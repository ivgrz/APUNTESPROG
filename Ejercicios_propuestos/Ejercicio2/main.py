import sys

from Hora import Hora

if __name__ == '__main__':

    hora1 = Hora(
        12, 30, 20
    )


    while True:
        print("==== HORAS ====")
        print(f"La hora actual es:\n"
              f" {hora1}")
        print(f"Que deseas hacer?: \n"
              f"1. Sumar segundos\n"
              f"2. Sumar minutos\n"
              f"3. Sumar horas\n"
              f"4. salir")
        opcion = int(input("> "))

        if opcion == 4:
            print("Saliendo del programa...")
            sys.exit() # Sales del programa como unn break
        try:
            if opcion == 1:
                try:
                    c_segundos = int(input(f"Cuantos segundos le quieres aumentar a {hora1}? "))
                    hora1.incrementar_segundos(c_segundos)
                except ValueError:
                    print("ERROR: SOLO VALORES ENTEROS")
            elif opcion == 2:
                try:
                    c_minutos = int(input(f"Cuantos minutos le quieres agregar a {hora1}? "))
                    hora1.incrementar_minutos(c_minutos)
                except ValueError:
                    print("ERROR: SOLO VALORES ENTEROS")
            elif opcion == 3:
                try:
                    c_horas = int(input(f"Cuantas horas le quieres agregar a {hora1}? "))
                    hora1.incrementar_horas(c_horas)
                except ValueError:
                    print("ERROR: SOLO VALORES ENTEROS")
            else:
                print("Opcion no valida, ingresa una de las que se muestran")

        except Exception as e:
            print(f"ERROR INESPERADO {e}")





