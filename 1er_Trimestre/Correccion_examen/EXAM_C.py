"""
GRUPO 1
Temperaturas...
tengo que poner freno a lo que se o me bajan puntos :):
"""


def temperaturas():
	ltemperaturas = []
	dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
	for dia in dias:
		temperatura = float(input(f"Añade la temperatura del dia {dia}: "))
		ltemperaturas.append(temperatura)

	return ltemperaturas


def valor_medio_temperaturas(temperaturas):
	if not temperaturas:
		return 0.0

	valor_medio = sum(temperaturas) / len(temperaturas)

	return valor_medio


def dias_media_temperatura(temperaturas):
	contador = 0
	media = valor_medio_temperaturas(temperaturas)

	for temperatura in temperaturas:
		if temperatura > media:
			contador += 1

	return contador

def mostrar_dias_superan_media(temperaturas, temperaturaLimite):
	dias = ["lunes","martes","miercoles","jueves","viernes"]
	for i, temperatura in enumerate(temperaturas):
		if temperatura > temperaturaLimite:
			return (f"El dia {dias[i]} supero el valor {temperaturaLimite}")


# De este modo se consigue usar la lista de la primera funcion en la segunda (llamando a las 2 en un menu)

if __name__ == "__main__":
	lista = temperaturas()
	media = valor_medio_temperaturas(lista)
	diassuperan = dias_media_temperatura(lista)
	qdiassuperan = mostrar_dias_superan_media(lista, media)
	print(f"El valor medio es {media}")
	print(f"La cantidad de dias que superan la media son: {diassuperan}")
	print(qdiassuperan)
