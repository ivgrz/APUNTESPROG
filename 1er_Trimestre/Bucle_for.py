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
# la variable que se toma como indice debe ser escrita siempre en singular
    for elemento in t:
        suma = suma + elemento
    print(f"La suma de todos los numeros es: {suma}")
print (f"===============================")
bucle_for2()

def bucle_for3():
    l = [1,2,3,4,5,6,7,8,9,10]
    suma = 0
    for i in range(0,8,3): #range(inicio, fin, salto)
        print(l[i])
print(f"===============================")

bucle_for3()

def bucle_for4():
    l = [1,2,3,4,5,6,7,8,9,10]
    print(f"Para la lista {l} usando enumerate quedaria como:")

    ordinal = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta", "Sexta", "Septima", "Octava", "Novena", "Decima"]



    for i, numero in enumerate(l): #enumerate da el indice y el valor de la lista
        # Concatenamos los ordinales con la lista de numeros
        print(f"En la {ordinal[i]} posicion, el indice es {i} y el numero es {numero}")

        if numero == 5:
            break
print(f"===============================")
bucle_for4()