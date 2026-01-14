class RegistroPersonas:
	def __init__(self):
		self._personas = []

	@property
	def personas(self):
		return self._personas
	@personas.setter
	def personas(self,personas):
		if isinstance(personas,list):
			self._personas = personas
		else:
			raise TypeError("Lista no encontrada")

	def agregar_personas(self,persona):
		self._personas.append(persona)
	def listar_personas(self):
		return list(self._personas)
	def __str__(self):
		return (f"----- REGISTRO PERSONAS -----\n"
				f""
				)