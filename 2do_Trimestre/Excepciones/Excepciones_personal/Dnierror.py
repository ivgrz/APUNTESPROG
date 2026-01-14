class Dnierror(Exception):
	def __init__(self, mensaje, dni = None):
		super().__init__()
		self.mensaje = mensaje
		self.dni = dni

	def __str__(self):
		return "Error: " + str(self.mensaje) + (f" (dni={self.dni})")

	@staticmethod
	def validar(dni):
		import re
		if not isinstance(dni, str):
			raise Dnierror(f"El dni debe ser una cadena", dni)

		s = dni.strip().upper()
		if not re.fullmatch(r"\d{8}[A-Z]",s):
			raise Dnierror(f"Formato de dni invalido, debe tener 8 digitos y una letra", dni)
		numero = int(s[:8])
		tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
		letra_esperada = tabla[numero % 23]
		if s[8] != letra_esperada:
			raise Dnierror("Letra de DNI no concuerda con lo esperado", dni)
		return True