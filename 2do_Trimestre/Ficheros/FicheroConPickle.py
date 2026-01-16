import json
import pickle
import datetime

fecha_hora = (datetime.datetime.now())
fecha, hora = str(fecha_hora).split()
print(f"{fecha} - {hora}")

amd = fecha.split('-')
hms = hora.split(':')

f_hora = {
	'anho' : amd[0],
	'mes' : amd[1],
	'dia' : amd[2],
	'hora' : hms[0],
	'minuto' : hms[1],
	'segundo' : hms[2]
}
# Pickle funciona para guardar cualquier tipo de objeto de Python en un fichero binario
# Guardamos el diccionario f_hora en el fichero fecha.dat
# 'wb' = write binary
# 'rb' = read binary
# 'ab' = append binary
# 'xb' = create binary
# 'b' = binary
# 't' = text
with open("fecha.dat", "wb") as fichero:
	pickle.dump(f_hora, fichero)
# Usamos .dump() para volcar el objeto en el fichero
with open("fecha.dat", "rb") as fichero:
# Usamos .load() para cargar el objeto del fichero
	dic = pickle.load(fichero)
	print(f"La hora de lectura es {dic['hora']} : {dic['minuto']} : {dic['segundo']} ")

opcionesUsuario = {
	'theme' : 'dark',
	'font_size' : 14,
	'show_line_numbers' : True
}

with open('opciones.dat','wb') as fich:
	pickle.dump(opcionesUsuario, fich)

with open('opciones.dat','rb') as fich:
	ops = pickle.load(fich)
	print(ops)