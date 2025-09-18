# Bucles basicos de python
def controltemp():
    temp = int(input("Dime la temperatura: "))


    while temp<100:
        print(f"Resistencia calefaccion encendida")
        temp += 10
        print(f"Temperatura actual: {temp}")
    else:
        print(f"Otra operacion")


if __name__ == "__main__":
    controltemp()