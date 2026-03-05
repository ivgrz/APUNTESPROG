from Producto import Producto
import csv


class Almacen:
    def __init__(self, ruta_fichero):
        self.ruta = ruta_fichero
        self.lista_productos = []
        self.cargar_producto(ruta_fichero)

    def cargar_producto(self, fichero):
        with open(fichero, 'r', newline='') as fich:
            readerP = csv.DictReader(fich)
            for linea_producto in readerP:
                p = Producto(linea_producto['nombre'],
                             int(linea_producto['cantidad']),
                             float(linea_producto['precio']))
                self.lista_productos.append(p)

    def anadir_producto(self):
        nombre = input("Nombre del producto a añadir: ")
        cantidad = int(input(f"Cuanto de {nombre} vas a añadir?: "))
        precio = float(input(f"Cuanto ha costado el producto {nombre}?: "))
        p = Producto(nombre, cantidad, precio)
        self.lista_productos.append(p)

    def guardar_producto(self, fichero):
        with open(fichero, 'w', newline='') as f:
            writerf = csv.DictWriter(
                f, fieldnames=['nombre', 'cantidad', 'precio'])
            writerf.writeheader()
            for p in self.lista_productos:
                writerf.writerow(
                    {'nombre': p.nombre, 'cantidad': p.cantidad, 'precio': p.precio})
