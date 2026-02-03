from Producto_ import Producto_
from Cliente import Cliente


class Pedido:
    def __init__(self, cliente: Cliente, fecha: str):

        self.__lista_productos = []
        self.setcliente(cliente)
        self.setfecha(fecha)

    def setlista_productos(self, lista_productos):
        self.__lista_productos = lista_productos

    def setcliente(self, cliente):
        self.__cliente = cliente

    def setfecha(self, fecha):
        self.__fecha = fecha

    def getlista_productos(self):
        return self.__lista_productos

    def getcliente(self):
        return self.__cliente

    def getfecha(self):
        return self.__fecha

    def anhadir_producto(self, producto: Producto_, cantidad: int):
        if cantidad > producto.getcantidad_stock():
            print("No hay suficiente stock")
            return False
        if not producto.decrementar_stock(cantidad):
            return False
        item = {
            "producto": producto,
            "cantidad": cantidad
        }
        self.__lista_productos.append(item)
        return True

    def eliminar_producto(self, producto: Producto_):
        for item in self.__lista_productos:
            if item["producto"] == producto:
                self.__lista_productos.remove(item)
                return True
        return False

    def calcular_precio_total(self):
        """Calcula el precio total del pedido"""
        total = 0.0
        for item in self.__lista_productos:
            producto = item["producto"]
            cantidad = item["cantidad"]
            total += producto.getprecio() * cantidad
        return total

    def calculo_IVA(self, porcentaje_IVA: float = 18.0):
        total_sin_IVA = self.calcular_precio_total()
        precio_iva = total_sin_IVA * (porcentaje_IVA / 100)
        return precio_iva

    def __str__(self):

        if not self.__lista_productos:
            return "La cesta está vacía"

        productos_str = ""
        for item in self.__lista_productos:
            producto = item["producto"]
            cantidad = item["cantidad"]
            subtotal = producto.getprecio() * cantidad
            productos_str += f"- {producto.getnombre()}\n"
            productos_str += f"  Cantidad: {cantidad}\n"
            productos_str += f"  Precio unitario: ${producto.getprecio():.2f}\n"
            productos_str += f"  Subtotal: ${subtotal:.2f}\n\n"

        # Retornar todo el string de una vez
        return f"""{'=' * 50}
=== PEDIDO ===
Cliente: {self.__cliente.getnombre()}
Email: {self.__cliente.getemail()}
Dirección: {self.__cliente.getdireccion()}, CP: {self.__cliente.getcod_p()}
Fecha: {self.__fecha}
{'=' * 10}

PRODUCTOS:
{productos_str}{'=' * 10}
TOTAL: ${self.calcular_precio_total():.2f}
{'=' * 10}"""

    lista_productos = property(getlista_productos, setlista_productos)
    cliente = property(getcliente, setcliente)
    fecha = property(getfecha, setfecha)
