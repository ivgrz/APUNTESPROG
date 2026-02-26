from equipo2 import Equipo
from EquipoNonExisteError2 import EquipoNonExisteError2
import csv


class Torneo2:
    def __init__(self, nome, num_max_eq=0, equipos_list=None):
        self.nome = nome
        self.num_max_eq = num_max_eq
        self.equipos_list = equipos_list
        self.num_equipos = len(self.equipos_list) if isinstance(
            self.equipos_list, list) else 0

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

    def add_equipo(self, equipo: Equipo):
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

                if l_aux[ind_max].get_puntos() < l_aux[i+1].get_puntos():
                    ind_max = i+1
            lClasificacion.append(l_aux.pop(ind_max))
        lClasificacion.append(l_aux[0])
        return lClasificacion

    def _find_team(self, name):
        for e in self.equipos_list:
            if isinstance(e, Equipo):
                if getattr(e, "nome", None) == name:
                    return e
                else:
                    if str(e) == name:
                        return e
        return None

    def registrar_encuentro(self, encuentro_resultado: str):
        """ Registra el resultado de un encuentro a partir de una cadena de texto
        :param encuentro_resultado: cadena con formato 'EquipoA-EquipoB N1-N2'
        :return:
        """
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
            n1, n2 = int(scores[0]), int(scores[1])
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

    def importar_resultados_fichero2(self, ruta):

        contador = 0
        with open(ruta, 'r', newline="") as fichero:
            fich_csv = csv.reader(fichero)
            for fila in fich_csv:
                contador += 1
                if contador == 1:
                    pass
                else:
                    local = fila[0]
                    visitante = fila[1]
                    rl = fila[2]
                    rv = fila[3]
                    cadena = f" {local} - {visitante} {rl} - {rv}"
                    print(cadena)
                """
                try:
                    self.registrar_encuentro(cadena)
                except ValueError as e:
                    print(e)
                """

    def importar_resultados_csv_diccionario(self, ruta):
        with open(ruta, 'r', newline="") as fichero:
            fich_csv = csv.DictReader(fichero)
            for fila in fich_csv:
                # print(fila)
                print(fila["Visitante"])

    def exportar_resultados_txt(self, ruta):
        """Crea un fichero .txt con los resultados en formato tabulado.
        Las columnas son las mismas que el CSV: Local, Visitante, Resultado local, Resultado visitante.
        El separador es el tabulador para que sea legible como texto plano.
        """
        with open(ruta, 'w', encoding='utf-8') as fichero:
            fichero.write(
                "Local\tVisitante\tResultado local\tResultado visitante\n")
            for equipo in self.equipos_list:
                fichero.write(
                    f"{equipo.nome}\t-\t{equipo.ganhados}\t{equipo.perdidos}\n")

    def importar_resultados_txt(self, ruta):
        """Importa resultados desde un fichero .txt con formato tabulado.
        Es el equivalente de importar_resultados_fichero2 pero para .txt.
        """
        with open(ruta, 'r', encoding='utf-8') as fichero:
            lineas = fichero.readlines()
            for i, linea in enumerate(lineas):
                if i == 0:
                    pass
                else:
                    partes = linea.strip().split('\t')
                    if len(partes) == 4:
                        local, visitante, rl, rv = partes
                        cadena = f"{local.strip()}-{visitante.strip()} {rl.strip()}-{rv.strip()}"
                        print(cadena)

                        # try:
                        #     self.registrar_encuentro(cadena)
                        # except ValueError as e:
                        #     print(e)

