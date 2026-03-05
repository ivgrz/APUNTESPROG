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
            print("3. Exportar copia en binario")
            print("4. Leer datos .pkl")
            print("5. Salir")

            opcion = input("Elige una opcion: ")
            match opcion:
                case '1':
                    self.mostrar_productos()
                case '2':
                    self.almacen.anadir_producto()
                case '3':
                    self.almacen.guardar_datos_binarios("productos.pkl")
                case '4':
                    self.almacen.leer_datos_binarios()
                case '5':
                    self.almacen.guardar_producto(self.almacen.ruta)
                    print("Guardando...")
                    break

    def mostrar_productos(self):
        print("\n---Lista Productos---")
        for producto in self.almacen.lista_productos:
            print(producto)
        print()
