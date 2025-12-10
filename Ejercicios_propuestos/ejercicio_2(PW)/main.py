from Hora import Hora

if __name__ == "__main__":
    # Creo ejemplos con varias entradas

    hora1 = Hora(10, 30, 45)
    hora2 = Hora("23:59:50")
    hora3 = Hora(14.575)
    hora4 = Hora(25, 61, 70)  # Comprobamos validacion

    print(hora1)
    print(hora2)
    print(hora3)
    print(hora4)
    print("--------------------------------\n")
    print("Probamos incremento de segundos:" + "\n"
          "Hora 1 antes: " + str(hora1)
          )
    # Llamamos al metodo

    hora1.incrementar_horas(2)
    print("Hora 1 despues de incrementar 2 horas: " + str(hora1))
