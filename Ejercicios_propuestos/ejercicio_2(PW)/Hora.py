class Hora:
    def __init__(self, hora=0, *minutoSegundo):
        # Comprobamos si el formato es int, int, int

        if isinstance(hora, int):
            self.__asignacion_variables_Int(hora, minutoSegundo)

        # Comprobamos si el formato es str
        if type(hora) == str:
            self.__asignacion_variables_Str(hora)
        # Comprobamos si el formato es list
        if isinstance(hora, list) or isinstance(hora, tuple):
            self.__asignacion_variables_Coleccion
        # Comprobamos si el formato es float
        if isinstance(hora, float):
            self.__asignacion_variables_Float

    def __asignacion_variables_Int(self, hora, minutoSegundo):
        self.setHora(hora)
        if minutoSegundo is not None:
            if len(minutoSegundo) == 1:
                if isinstance(minutoSegundo[0], int):
                    self.setMinuto(minutoSegundo[0])
            elif len(minutoSegundo) == 2:
                if isinstance(minutoSegundo[0], int):
                    self.setMinuto(minutoSegundo[0])
                if isinstance(minutoSegundo[1], int):
                    self.setSegundo(minutoSegundo[1])

        def __asignacion_variables_Str(self, hora):
			if len(hora) == 8:
				if hora[2] == ':' and hora[5] == ':':
					hms = hora.split(':')

					if hms[0].isnumeric():
						h = int(hms[0])
						if 0 <= h <= 24:
							self.setHora(h)
					if hms[1].isnnumeric():
						m = int(hms[1])
						if 0 <= m <= 59:
							self.setMinuto(m)
					if hms[2].isnumeric():
						s = int(hms[2])
						if 0 <= s <= 59:
							self.setSegundo(s)
			else:
				self.setHora(0)
				self.minuto(0)
				self.segundo(0)
