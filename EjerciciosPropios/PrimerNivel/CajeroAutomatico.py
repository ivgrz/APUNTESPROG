class CajeroAutomatico():
    def __init__(self, saldo=0):
        self.saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):

        self.__saldo = saldo

    def consultar_saldo(self, saldo_c):
        self.saldo = saldo_c

        return saldo_c

    def ingresar_dinero(self, dinero):
        if dinero > 0:
            self.saldo += dinero
        return self.saldo

    def retirar_dinero(self, retiro):
        if retiro < self.saldo:
            self.saldo -= retiro
        return self.saldo


if __name__ == "__main__":
    cajero = CajeroAutomatico()

    while True:

        print("1. Consultar Saldo")
        print("2. Ingresar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = int(input("Elige una opcion: "))
        if opcion == 1:
            saldo_i = 1000
            print(f"Tu saldo es de: {cajero.consultar_saldo(saldo_i)}")

        elif opcion == 2:
            ingreso = int(input("Ingresa la cantidad: "))
            print(f"Tu nuevo saldo es de: {cajero.ingresar_dinero(ingreso)}")
        elif opcion == 3:
            retiro = int(input("Indica la cantidad que quieres retirar: "))
            print(f"Tu nuevo saldo es de: {cajero.retirar_dinero(retiro)}")
        elif opcion == 4:
            print("Saliendo...")
            break
