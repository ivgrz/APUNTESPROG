def Conversion_grados():
    grados_c = int(input("Dame los °C a convertir: "))
    grados_farenheit = grados_c * (9/5) + 32
    print(grados_farenheit.__round__(2))
    grados_kelvin = grados_c + 32
    print(grados_kelvin.__round__(2))


if __name__ == "__main__":
    Conversion_grados()
