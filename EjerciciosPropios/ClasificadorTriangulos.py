def clasif_triangulos():
    lados = input("Dame los lados del triangulo en formato 'l1,l2,l3': ")
    l1, l2, l3 = lados.split(',')
    comprobacion_t = int(l1) + int(l2)
    l3n = int(l3)
    if not comprobacion_t > l3n:
        raise ValueError("Triangulo invalido")
    elif l1 == l2 and l1 == l2 and l2 == l3 and l2 == l1 and l3 == l1 and l3 == l2:
        print("Triangulo equilatero")
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print("Es un triangulo isosceles")
    elif l1 != l2 != l3:
        print("Es un triangulo escaleno")


if __name__ == "__main__":
    clasif_triangulos()
