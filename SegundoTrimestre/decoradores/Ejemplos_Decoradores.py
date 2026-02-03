def decorador2(func):
	def envoltorio(*args, **kwargs):
		print("Antes de la función decorada 2")
		resultado = func(*args, **kwargs)
		print("Después de la función decorada 2")
		return resultado
	return envoltorio() 
