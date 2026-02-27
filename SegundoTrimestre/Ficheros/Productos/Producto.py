class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            self.__nombre = ""
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
        if isinstance(cantidad, int):
            self.__cantidad = cantidad
        else:
            self.__cantidad = 0
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio):
        if isinstance(precio, float):
            self.__precio = precio
        else:
            self.__precio = 0

    def valor_stock(self):
        valor_stock = self.cantidad * self.precio
        return valor_stock

    def __str__(self):
        return f"Producto: {self.nombre} | Cantidad: {self.cantidad} | Precio: {self.precio} | Valor de stock: {self.valor_stock()}"