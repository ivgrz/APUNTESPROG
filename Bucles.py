"""
BUCLES BASICOS DE PYTHON
"""
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

def bucle_for1():

    t = (1,2,3,4,5,6,7,8,9,10)
    i = 0
    suma = 0
    while i <= 7:
        suma = suma + t[i]
        i += 1
# i += 1 realiza incremento en 1 la variable i
    print(f"La suma de los primeros 8 numeros es: {suma}")
bucle_for1()
def bucle_for2():
    t = (1,2,3,4,5,6,7,8,9,10)
    suma = 0
    for elemento in t:
        suma = suma + elemento
    print(suma)
bucle_for2()