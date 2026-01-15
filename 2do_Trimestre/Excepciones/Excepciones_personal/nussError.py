
class nussError(Exception):
	def __init__(self, mensaje, nuss):
		super().__init__(mensaje)
		self.mensaje = mensaje
		self.nuss = nuss

	def __str__(self):
		return "Error: " + str(self.mensaje) + (f" (nuss={self.nuss}" if self.nuss else "")

	@staticmethod
	def validar(nuss):
		if not isinstance(nuss, str):
			raise nussError("El nuss debe ser una cadena", nuss)

		s = nuss.strip()
		if len(s) != 16:
			raise nussError("El nuss debe contener 16 caracteres", nuss)

		pos1 = 2
		pos2 = len(s) - 3
		if s[pos1] != '/' or s[pos2] != '/':
			raise nussError("El formato del NUSS es nn/nnnnnnnnnnnn/nn", nuss)
		for i, char in enumerate(s):
			if i == pos1 or i == pos2:
				continue
			if not char.isdigit():
				raise nussError(f"Caracter no valido en posicion {i}: todos los caracteres deben ser digitos", nuss)
			return True
		return None