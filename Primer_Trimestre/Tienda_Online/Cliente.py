class Cliente:
	def __init__(self, nombre: str, email: str, direccion:str, cod_p:int):
		self.setnombre(nombre)
		self.setemail(email)
		self.setdireccion(direccion)
		self.setcod_p(cod_p)

	def setnombre(self, nombre):
		self.__nombre = nombre
	def setemail(self, email):
		self.__email = email
	def setdireccion(self, direccion):
		self.__direccion = direccion
	def setcod_p(self, cod_p):
		self.__cod_p = cod_p

	def getnombre(self):
		return self.__nombre
	def getemail(self):
		return self.__email
	def getdireccion(self):
		return self.__direccion
	def getcod_p(self):
		return self.__cod_p






	nombre = property(getnombre,setnombre)
	email = property(getemail,setemail)
	direccion = property(getdireccion,setdireccion)
	codigo_postal = property(getcod_p,setcod_p)