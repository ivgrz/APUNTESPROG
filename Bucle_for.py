"""
DOS MANERAS DE HACER UN BUCLE FOR
"""
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
    print(f"La suma de todos los numeros es: {suma}")
bucle_for2()