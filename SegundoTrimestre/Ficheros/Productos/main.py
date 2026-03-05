from Almacen import Almacen
from Producto import Producto
from Gestion_Almacen import Gestion_Almacen
if __name__ == '__main__':

    a = Almacen('/Users/vnangz/Library/CloudStorage/GoogleDrive-ivangxz1403@gmail.com/Mi unidad/APUNTESPROG/SegundoTrimestre/Ficheros/Productos/Producto.csv')
    g = Gestion_Almacen(a)
    g.menu()
