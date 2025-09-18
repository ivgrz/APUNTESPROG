

#Condicionales basicos
def condiciones(temp, porcNubes, precipitacion):
    if temp > 16 and porcNubes < 40 and precipitacion == 0:

        print(f"Hace calor, deberias: ")
        print ("Agarrar toalla")
        print("Poner bañador")
        print("ir a playa")
    else:

        print("Hace frio, deberias: ")
        print("Quedarte en casa")
        print("Ver Netflix")
        print("Comer palomitas")

def main():

    print("¿Que planes hay por hacer hoy?")
    temp = input("Dime la temperatura: ")
    porcNubes = input("Dime el porcentaje de nubes: ")
    precipitacion = input("Dime la precipitacion: ")


    condiciones(int(temp), int(porcNubes), int(precipitacion))

if __name__ == "__main__":
    main()