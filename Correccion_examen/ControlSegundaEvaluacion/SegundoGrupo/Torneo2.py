from Correccion_examen.ControlSegundaEvaluacion.SegundoGrupo.equipo2 import Equipo
from EquipoNonExisteError2 import EquipoNonExisteError2

class Torneo2:
	def __init__(self, nome, num_max_eq=0, equipos_list=None):
		self.nome = nome
		self.num_max_eq = num_max_eq
		self.equipos_list = equipos_list
		self.num_equipos = len(self.equipos_list)

	@property
	def nome(self):
		return self.__nome
	@nome.setter
	def nome(self, nome):
		if isinstance(nome, str):
			self.__nome = nome
		else:
			self.__nome = ""

	@property
	def num_max_eq(self):
		return self.__num_max_eq
	@num_max_eq.setter
	def num_max_eq(self, num_max_eq):
		if isinstance(num_max_eq, int):
			self.__num_max_eq = num_max_eq
		else:
			self.__num_max_eq = 0

	@property
	def equipos_list(self):
		return self.__equipos_list
	@equipos_list.setter
	def equipos_list(self, equipos_list):
		if isinstance(equipos_list, list):
			self.__equipos_list = equipos_list
		else:
			self.__equipos_list = []

	@property
	def num_equipos(self):
		return self.__num_equipos
	@num_equipos.setter
	def num_equipos(self, num_equipos):
		if isinstance(num_equipos, int):
			self.__num_equipos = num_equipos
		else:
			self.__num_equipos = 0

	def add_equipo(self, equipo:Equipo):
		if not isinstance(equipo, Equipo):
			return -1
		if self.num_max_eq > 0 and len(self.equipos_list) >= self.__num_max_eq:
			return -1
		if equipo in self.equipos_list:
			return -1
		self.equipos_list.append(equipo)
		self.num_equipos = len(self.equipos_list)
		return self.equipos_list
	def get_equipo(self):
		return self.equipos_list
	def get_clasificacion(self):
		l_aux = self.equipos_list[:]
		lClasificacion = []

		while len(l_aux) > 1:
			ind_max = 0
			for i in range(len(l_aux)-1):
				if l_aux[ind_max].equipo.get_puntos()<l_aux[i+1].equipo.get_puntos():
					ind_max = i+1
			lClasificacion.append(l_aux.pop(ind_max))
		lClasificacion.append(l_aux[0])
		return lClasificacion



	def registrar_encuentro(self, encuentro_resultado:str):
		partes = encuentro_resultado.strip().split()
		if len(partes) != 2:
			raise ValueError("Formato incorrecto: 'EquipoA-EquipoB N1-N2'")
		equipos_p, scores_p = partes
		equipos = equipos_p.split('-')
		scores = scores_p.split('-')
		if len(equipos) != 2 or len(scores) != 2:
			raise ValueError("Formato invalido")
		e1, e2 = equipos[0].strip(), equipos[1].strip()
		try:
			n1,n2 = int(scores[0]), int(scores[1])
		except ValueError:
			raise ValueError("Los resultados deben ser números enteros")
		e1 = self._find_team(e1)
		e2 = self._find_team(e2)
		if e1 is None or e2 is None:
			raise EquipoNonExisteError2()
		if n1 > n2:
			print(f"Gana el equipo {e1}")
		elif n1 < n2:
			print(f"Gana el equipo {e2}")
		else:
			print("Empate")


		def _find_team(name):
			for e in self.equipos_list:
				if isinstance(e, Equipo):
					if getattr(e, "nome", None) == name:
						return e
					else:
						if str(e) == name:
							return e
			return None


