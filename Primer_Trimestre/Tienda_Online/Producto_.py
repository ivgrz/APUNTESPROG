from typing import List, Dict, Any, Optional


class Producto_:
    def __init__(self, nombre: str, precio: float, cantidad_stock: int):
        self.setnombre(nombre)
        self.setprecio(precio)
        self.setcantidad_stock(cantidad_stock)

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setprecio(self, precio):
        self.__precio = precio

    def setcantidad_stock(self, cantidad):
        if isinstance(cantidad, int) and cantidad > 0:
            self.__cantidad_stock = cantidad

        else:
            print("Error: La cantidad debe ser un numero entero")
            self.__cantidad_stock = 0

    def getnombre(self):
        return self.__nombre

    def getprecio(self):
        return self.__precio

    def getcantidad_stock(self):
        return self.__cantidad_stock

    def decrementar_stock(self, cantidad):

        if not isinstance(cantidad, int) or cantidad <= 0:
            print("Error: La cantidad debe ser entera y positiva")
            return False
        if cantidad > self.getcantidad_stock():
            print(
                f"Entrada no valida: solo hay {self.getcantidad_stock()} en stock")
            return False

        self.__cantidad_stock -= cantidad
        return True

    def incrementar_stock(self, cantidad):

        if not isinstance(cantidad, int) or cantidad <= 0:
            print("La cantidad debe ser un entero y positivo")
            return None
        self.__cantidad_stock += cantidad
        return self.__cantidad_stock

    nombre = property(getnombre, setnombre)
    precio = property(getprecio, setprecio)
    cantidad = property(getcantidad_stock, setcantidad_stock)
