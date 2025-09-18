# Bucles basicos de python
# Funcion con while y else
def controltemp():
    temp = int(input("Dime la temperatura: "))


    while temp<100:
        print(f"Resistencia calefaccion encendida")
        temp += 10
        print(f"Temperatura actual: {temp}")
    else:
        print(f"Otra operacion")

controltemp()

# Funcion con while segundo ejemplo
def contar():
    cont = 0

    while cont <= 20:
        print(cont)
        cont += 3
    if cont >= 21:
        print("Hemos llegado al final del bucle")


contar()

# Funcion con while true, break y continue
def bucle_whiletrue():
    cont = 0
    while True:
        cont += 1
        if cont%3 != 0:
            continue
        print(cont)
        if cont > 20:
            break
bucle_whiletrue()

