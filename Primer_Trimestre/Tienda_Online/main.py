from Pedido import Pedido
from Producto_ import Producto_
from Cliente import Cliente

if __name__ == '__main__':

    cliente1 = Cliente("Juan Perez", "juan.p@gmail.com", "Calle A", 36320)
    pedido1 = Pedido(cliente1, "11/11/2025")

    pedido1.anhadir_producto(Producto_("Zapato", 50.45, 10), 1)
    pedido1.anhadir_producto(Producto_("camiseta", 20.30, 50), 2)
    print(pedido1)
    print(f"Precio total {pedido1.calcular_precio_total()}")
