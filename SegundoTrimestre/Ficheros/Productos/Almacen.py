from Producto import Producto
import csv
class Almacen:
    def __init__(self, ruta_fichero):
        self.lista_productos = []
        self.cargar_producto(ruta_fichero)


    def cargar_producto(self, fichero):
        with open(fichero,'r', newline='') as fich:
            readerP = csv.DictReader(fich)
            for linea_producto in readerP:
                p = Producto(linea_producto['nombre'],
                         int(linea_producto['cantidad']),
                         float(linea_producto['precio']))
                self.lista_productos.append(p)







