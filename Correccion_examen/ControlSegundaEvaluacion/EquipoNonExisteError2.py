class EquipoNonExisteError2(Exception):
	"""Excepción lanzada cuando un equipo buscado no existe en el torneo.

	Opcionalmente puede proporcionarse el nombre del equipo no existente para
	construir un mensaje más informativo.
	"""
	def __init__(self, nombre_equipo=None, mensaje=None):
		if mensaje is None:
			if nombre_equipo:
				mensaje = f"El equipo '{nombre_equipo}' no existe en el torneo."
			else:
				mensaje = "Uno o más equipos no existen en el torneo."
		super().__init__(mensaje)
		self.nombre_equipo = nombre_equipo

	def __str__(self):
		# devolver el mensaje de la excepción
		return super().__str__()
