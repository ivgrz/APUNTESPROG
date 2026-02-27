from Almacen import Almacen

class Gestion_Almacen:
    def __init__(self):
        self.almacen = Almacen('/home/dam/Escritorio/apuntesprog/SegundoTrimestre/Ficheros/Productos/Producto.csv')

    def menu(self):
        while True:
            print("Programa de Gestion de Almacenes")
            print("__________________________________")
            print("1. Listar Productos")
            print("2. Salir")

            opcion = input("Elige una opcion: ")
            match opcion:
                case '1':
                    self.mostrar_productos()
                case '2':
                    break
    def mostrar_productos(self):
        print("\n---Lista Productos---")
        for producto in self.almacen.lista_productos:
            print(producto)
        print()
