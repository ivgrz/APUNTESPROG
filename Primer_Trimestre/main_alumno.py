from alumno import Alumno
from persona import Persona
def leer_contador():
	c = getattr(Alumno, 'contador_alumnos', None)
	if c is None and hasattr(Alumno, 'contar_alumnos'):
		c = Alumno.contador_alumnos()
	return c if c is not None else 0

if __name__ == "__main__":

	print(f"Hay {leer_contador()} alumnos")


	alumno1 = Alumno("Raul", 20, "12345679A", "Calle A 123",
                     "Brasilera", "01/01/2000", "DAM")
	alumno2 = Alumno("Ana", 22, "37287456B", "Calle B 456",
                     "Española", "02/02/2004", "DAW")

	print(f"Se han creado correctamente los alumnos:\n{alumno1}\n{alumno2}")
	print(f"Ahora hay {leer_contador()} alumnos")


