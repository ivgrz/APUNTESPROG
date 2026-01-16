import datetime

# 1. Intentamos leer el archivo de ejercicios
fichero = None
try:
    # Ruta de tu archivo
    fichero = open('/Users/vnangz/Library/CloudStorage/GoogleDrive-ivangxz1403@gmail.com/Mi unidad/APUNTESPROG/1er_Trimestre/Ejercicio1/Ejercicio_Ahorcado.py', 'r')
    for linea in fichero:
        print(linea)
except:
    print("Error: No se pudo abrir el archivo de lectura")
finally:
    # Solo cerramos si realmente se logró abrir
    if fichero != None:
        fichero.close()


# 2. Obtenemos la fecha y hora
fecha_hora = datetime.datetime.now()
fecha, hora = str(fecha_hora).split()


# 3. Escribimos en el archivo saludo1.txt
# Usamos 'a' para AÑADIR en lugar de 'w' para borrar/escribir
fichero = open('saludo1.txt', 'a')

fichero.write("\nHola, soy Yo\n")
fichero.write(fecha + "\n")
fichero.write(hora + "\n")
fichero.write("Termino y añado contenido al fichero\n")

fichero.close()

print("Proceso finalizado con éxito.")

fichero = open('saludo1.txt', 'rb')
lectura = fichero.readline()
while linea != "":

    print(linea)
    linea = fichero.readline()

fichero.close()

fichero = open('saludo1.txt', 'r')
lectura = fichero.readlines()
print(lectura)
fichero.close()
# De esta manera no hay que cerrar explicitamente el fichero
with open ('saludo1.txt', 'r') as fichero:
    l = 0
    for linea in fichero:
        l += 1
    print(f"El fichero tiene {l} lineas")




