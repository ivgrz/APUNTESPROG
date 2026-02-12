class JugadorNoExisteError(Exception):
	def __init__(self, mensaje, jugador):
		super().__init__(mensaje)
		self.mensaje = mensaje
		self.jugador = jugador

	def __str__(self):
		return "Error: " + str(self.mensaje)
