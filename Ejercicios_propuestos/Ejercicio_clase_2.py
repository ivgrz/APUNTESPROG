"""
Hacer un programa que devuelva una contraseña
De 6 a 12 caracteres
Letras minusculas y mayusculas aleatoriamente
incluye simbolos y numeros
"""
import random
import string

def generador_contrasena():
    # Usamos random.randint para generar un numero aleatorio entre 6 y 12 que va a ser la longitud final de la contraseña

    longitud = random.randint(6,12) #Generamos una cadena aleatoria de valores con los parametros entre 6 y 12

    #Conjunto de caracteres permitidos

    letras_minus = string.ascii_lowercase # Usamos string.ascii_lowercase para obtener todas las letras minusculas

    letras_mayus = string.ascii_uppercase # Usamos string.ascii_uppercase para obtener todas las letras mayusculas

    numeros = string.digits # Usamos string.digits para obtener todos los digitos del 0 al 9

    simbolos = string.punctuation # Usamos string.punctuation para obtener todos los simbolos

    # Unimos todos los caracteres permitidos

    todos = letras_minus + letras_mayus + numeros + simbolos

    # Generamos una contraseña aleatoria con estos parametros

    contrasena = ''
    # Cuando usamos in range(longitud), la variable i toma valores desde 0 hasta longitud-1
    for i in range(longitud):
        # Elegimos cualquier caracter de los permitidos
        caracter_aleatorio = random.choice(todos)
        # Usamos random.choice para elegir un caracter aleatorio de la cadena 'todos'
        contrasena += caracter_aleatorio
        # Usamos += para ir concatenando los caracteres aleatorios a la variable contrasena
    return contrasena
        # Devolvemos la contraseña generada

print(f"Contraseña generada: {generador_contrasena()}")
