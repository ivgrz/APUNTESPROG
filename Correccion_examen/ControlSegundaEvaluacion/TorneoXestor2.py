from Correccion_examen.ControlSegundaEvaluacion.Torneo2 import Torneo2
from Correccion_examen.ControlSegundaEvaluacion.equipo2 import Equipo
from Correccion_examen.ControlSegundaEvaluacion.EquipoNonExisteError2 import EquipoNonExisteError2

class Torneo_Gestor:
	# inicializar con un nombre por defecto para evitar error al crear Torneo2 sin argumentos
	torneo = Torneo2("Torneo")
	def __init__(self):
		pass

	def mostrar_menu(self):
		print("\n--- MENU TORNEO ---")
		print("1. Registrar encuentro (Formato: EquipoA-EquipoB N1-N2)")
		print("2. Mostrar clasificación")
		print("3. Añadir equipo")
		print("4. Listar equipos")
		print("5. Salir")

	def bucle_principal(self):
		opcion = 0
		while(opcion != 5):
			self.mostrar_menu()
			try:
				opcion = int(input("Elige una opcion: "))
			except ValueError:
				print("Por favor introduce un número válido entre 1 y 5")
				continue
			match (opcion):
				case 1 :
					encuentro_resultado = input("Escribe el resultado del encuentro: ")
					try:
						self.torneo.registrar_encuentro(encuentro_resultado)
					except ValueError as ve:
						print(f"Error en formato o valores: {ve}")
					except EquipoNonExisteError2:
						print("Error: algún equipo no existe en el torneo")
					except Exception as e:
						print(f"Error inesperado: {e}")
				case 2:
					equipos_ordenados = self.torneo.get_clasificacion()
					for i, equipo in enumerate(equipos_ordenados):
						# algunos implementaciones pueden envolver el objeto con atributo 'equipo'
						if hasattr(equipo, 'equipo'):
							team = equipo.equipo
						else:
							team = equipo
						print(f"{i+1}. {team.nome} - {team.get_puntos()} puntos")
				case 3:
					nombre = input("Nombre del equipo a añadir: ")
					if not nombre.strip():
						print("Nombre no válido")
						continue
					eq = Equipo(nombre.strip())
					res = self.torneo.add_equipo(eq)
					if res == -1:
						print("No se pudo añadir el equipo (ya existe o se ha alcanzado el máximo)")
					else:
						print(f"Equipo '{nombre}' añadido correctamente")
				case 4:
					equipos = self.torneo.get_equipo()
					if not equipos:
						print("No hay equipos en el torneo")
					else:
						for i, equipo in enumerate(equipos):
							if hasattr(equipo, 'equipo'):
								team = equipo.equipo
							else:
								team = equipo
							print(f"{i+1}. {team.nome} - {team.get_puntos()} puntos")
				case 5:
					print("Saliendo...")
					break
				case _:
					print("Opción no válida")
