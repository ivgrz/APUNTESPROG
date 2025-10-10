"""
Hacer un programa que devuelva una contraseña
De 6 a 12 caracteres
Letras minusculas y mayusculas aleatoriamente
incluye simbolos y numeros
"""
import random
import string

def generador_contrasena():

    longitud = random.randint(6,12) #Generamos una cadena aleatoria de valores con los parametros entre 6 y 12

    #Conjunto de caracteres permitidos

    letras_minus = string.ascii_lowercase
    letras_mayus = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    # Unimos todos los caracteres permitidos

    todos = letras_minus + letras_mayus + numeros + simbolos

    # Generamos una contraseña aleatoria con estos parametros

    contrasena = ''

    for i in range(longitud):
        caracter_aleatorio = random.choice(todos) # Elegimos cualquier caracter de los permitidos
        contrasena += caracter_aleatorio
    return contrasena

print(f"Contraseña generada: {generador_contrasena()}")
