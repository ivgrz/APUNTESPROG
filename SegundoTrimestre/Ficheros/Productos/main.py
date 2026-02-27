from Almacen import Almacen
from Producto import Producto
from Gestion_Almacen import Gestion_Almacen
if __name__ == '__main__':


    a = Almacen('/home/dam/Escritorio/apuntesprog/SegundoTrimestre/Ficheros/Productos/Producto.csv')
    g = Gestion_Almacen()
    g.menu()