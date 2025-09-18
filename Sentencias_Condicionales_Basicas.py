

#Sentencias Condicionales basicas


#Definimos una funcion
def condiciones(temp, porcNubes, precipitacion):

#Primer condicional IF
    if temp > 16 and porcNubes < 40 and precipitacion == 0:
        print("Hace buen tiempo, deberias: ")
        print ("Agarrar toalla")
        print("Poner bañador")
        print("ir a playa")

#Caso contrario ELSE
    else:

        print("Hace frio, deberias: ")
        print("Quedarte en casa")
        print("Ver Netflix")
        print("Comer palomitas")
    if temp < 0:
        print(f"Hace un monton de frio")

# Elif es un else if
    elif temp > 0 and temp < 10:
        print(f"Hace frio")
    elif temp >= 10 and temp < 20:
        print(f"Hace una temperatura agradable")
    elif temp >= 20 and temp < 30:
        print(f"Esta templado")
    elif temp >= 30:
        print(f"Hace muchisimo calor")


#Definimos la funcion main
def main():

# Preguntamos al usuario para ingreso de datos
    print("¿Que planes hay por hacer hoy?")
    temp = input("Dime la temperatura: ")
    porcNubes = input("Dime el porcentaje de nubes: ")
    precipitacion = input("Dime la precipitacion: ")

# Llamamos a la funcion
    condiciones(int(temp), int(porcNubes), int(precipitacion))


#Mostramos la funcion main por pantalla
if __name__ == "__main__":
    main()

"""
Maneras de simplificar condicionales:

    if temp > 15:
        valoracion_Atmosferica = "Calor"
    else:
        valoracion_Atmosferica = "Frio"

    Valoracion_Atmosferica = "Calor" if temp > 15 else "Frio"

    EN JAVA ==> Valoracion_Atmosferica = (temp > 15) ? "Calor" : "Frio";
"""
