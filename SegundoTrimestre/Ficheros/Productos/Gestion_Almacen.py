from Almacen import Almacen


class Gestion_Almacen:
    def __init__(self, almacen):
        self.almacen = almacen

    def menu(self):
        while True:
            print("Programa de Gestion de Almacenes")
            print("__________________________________")
            print("1. Listar Productos")
            print("2. Añadir Producto")
            print("3. Salir")

            opcion = input("Elige una opcion: ")
            match opcion:
                case '1':
                    self.mostrar_productos()
                case '2':
                    self.almacen.anadir_producto()
                case '3':
                    self.almacen.guardar_producto(self.almacen.ruta)
                    break

    def mostrar_productos(self):
        print("\n---Lista Productos---")
        for producto in self.almacen.lista_productos:
            print(producto)
        print()
