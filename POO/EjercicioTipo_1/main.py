from POO.EjercicioTipo_1.Cilindro import Cilindro
from POO.EjercicioTipo_1.Esfera import Esfera
from circulo import Circulo
from punto import Punto
from persona import Persona
from Cilindro import Cilindro
from Esfera import Esfera
from cono import Cono
from Tronco_cono import Cono_truncado
from Punto2 import Punto2
from Fecha import Fecha
import sys

def solicitar_fecha_nacimiento():
	print("\n--- INGRESO DE FECHA DE NACIMIENTO ---")

	# 1. Solicitar los datos al usuario
	try:
		dia = int(input("Introduce el día de nacimiento (ej. 15): "))
		mes = int(input("Introduce el mes de nacimiento (ej. 10): "))
		anho = int(input("Introduce el año de nacimiento (ej. 1990): "))
	except ValueError:
		# Maneja el caso en que el usuario no introduce un número
		print("\nERROR: Día, Mes y Año deben ser números enteros. Terminando el programa.")
		sys.exit(1)

	# 2. Crear el objeto Fecha
	# La clase Fecha internamente valida si la fecha es posible (ej. no 30/02)
	fecha_objeto = Fecha(dia, mes, anho)

	print("\nValidation de Fecha completada.")
	return fecha_objeto



def solicitar_datos_persona(fecha_nac):
	print("\n--- INGRESO DE DATOS PERSONALES ---")

	# Datos de Persona
	nombre = input("Introduce el Nombre: ")

	# Intentar convertir edad a entero
	try:
		edad = int(input("Introduce la Edad: "))
	except ValueError:
		edad = -1  # Un valor que forzará la edad a 0 en el constructor de Persona
		print("Advertencia: Edad inválida, se establecerá a 0.")

	dni = input("Introduce el DNI (ej. 12345678A): ")
	direccion = input("Introduce la Dirección: ")
	nacionalidad = input("Introduce la Nacionalidad: ")

	# Crear el objeto Persona, pasándole el objeto Fecha validado
	try:
		nueva_persona = Persona(nombre, edad, dni, direccion, nacionalidad, fecha_nac)
		return nueva_persona
	except Exception as e:
		print(f"\nERROR al crear la Persona: {e}")
		sys.exit(1)







if __name__ == '__main__':
	print(f"\n---FIGURAS---\n")

	c = Circulo(4, 3, 5)
	print(c.Cadena())

	ci = Cilindro(4, 3, 5, 6)
	print(ci.Cadena())

	esf = Esfera(4, 3, 5)
	print(esf)

	cono = Cono(4, 3, 5, 6)
	print(cono)

	cono_t = Cono_truncado(4, 3, 8, 6, 5)
	print(cono_t)

	print(f"> PUNTO:")

	p1 = Punto(2, 3)
	p1.x = -2
	p2 = Punto(9, 1)

	p3 = Punto2(3, 4)

	p3.x = 3
	print(p3)
	print(p3.x)
	print(p3.gety())


	fecha_nacimiento_p = solicitar_fecha_nacimiento()
	persona_creada = solicitar_datos_persona(fecha_nacimiento_p)


	print(f"\n==================="
		  f"\nOBJETO CREADO EXITOSAMENTE\n"
		  f"{persona_creada}\n"
		  f"====================")
	if persona_creada.dni == "00000000X":
		print("AVISO: El DNI introducido no era válido y se usó el valor por defecto.")

