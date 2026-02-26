import csv




class torneo:
	def importar_resultados_fichero2(self, ruta):
		contador = 0
		with open(ruta, 'r', newline="") as fichero:
			fich_csv = csv.reader(fichero)
			for fila in fich_csv:
				contador +=1
				if contador == 1:
					pass
				else:
					visitante = fila[1]
					local = fila[0]
					rl = fila[2]
					rv = fila[3]
					cadena = f" {local} - {visitante} {rl} - {rv}"
					print(cadena)


	def registar_encuentro(self, cadena):
		pass

if __name__ == '__main__':
	t = torneo()
t.importar_resultados_fichero2('/Users/vnangz/Library/CloudStorage/GoogleDrive-ivangxz1403@gmail.com/Mi unidad/APUNTESPROG/Correccion_examen/ControlSegundaEvaluacion/SegundoGrupo/resultados4xornada.csv')