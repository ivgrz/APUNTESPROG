class TablaMultiplicar:
    def __init__(self, numero, inicio, fin):
        self.numero = numero
        self.inicio = inicio
        self.fin = fin

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        if numero > 0:
            self.__numero = numero
        else:
            self.__numero = 0

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio):
        if inicio > 0:
            self.__inicio = inicio

        else:
            self.__inicio = 0

    @property
    def fin(self):
        return self.__fin

    @fin.setter
    def fin(self, fin):
        if fin > 0:
            self.__fin = fin
        else:
            self.__fin = 0

    def multiplicacion(self):
        for i in range(self.inicio, self.fin+1):

            print(f" {self.numero} x {i} = {self.numero * i} ")

    def __str__(self):
        return str(self.multiplicacion())


if __name__ == "__main__":
    numero = int(input("Ingresa un numero entero: "))
    inicio = int(input("Ingresa el inicio del rango: "))
    fin = int(input("Ingresa el fin del rango: "))

    t1 = TablaMultiplicar(numero, inicio, fin)
    print(t1)
