class Hora:
    """Clase para representar y manipular horas en formato HH:MM:SS"""

    def __init__(self, hora=0, *minutoSegundo):
        """
        Constructor que acepta múltiples formatos de entrada

        :param hora: Puede ser int, str, list, tuple o float
        :param minutoSegundo: Minutos y segundos opcionales (solo para int)
        """
        # Inicializar atributos usando setters
        self.setHora(0)
        self.setMinuto(0)
        self.setSegundo(0)

        # Comprobamos el tipo y llamamos al método que le corresponde
        if isinstance(hora, int):
            self.__asignacion_variables_Int(hora, minutoSegundo)
        elif isinstance(hora, str):
            self.__asignacion_variables_Str(hora)
        elif isinstance(hora, (list, tuple)):
            self.__asignacion_variables_Coleccion(hora)
        elif isinstance(hora, float):
            self.__asignacion_variables_Float(hora)

    def __asignacion_variables_Int(self, hora, minutoSegundo):
        """Asigna valores desde enteros"""
        self.setHora(hora)
        if minutoSegundo is not None:
            if len(minutoSegundo) >= 1:
                self.setMinuto(minutoSegundo[0])
            if len(minutoSegundo) >= 2:
                self.setSegundo(minutoSegundo[1])

    def __asignacion_variables_Str(self, hora):
        """Asigna valores desde string formato HH:MM:SS"""
        if len(hora) == 8 and hora[2] == ':' and hora[5] == ':':
            hms = hora.split(':')

            if hms[0].isnumeric():
                self.setHora(int(hms[0]))
            if hms[1].isnumeric():
                self.setMinuto(int(hms[1]))
            if hms[2].isnumeric():
                self.setSegundo(int(hms[2]))
        else:
            self.setHora(0)
            self.setMinuto(0)
            self.setSegundo(0)

    def __asignacion_variables_Coleccion(self, colec):
        """Asigna valores desde lista o tupla"""
        if len(colec) >= 1:
            self.setHora(colec[0])
        if len(colec) >= 2:
            self.setMinuto(colec[1])
        if len(colec) >= 3:
            self.setSegundo(colec[2])

    def __asignacion_variables_Float(self, hora):
        """Asigna valores desde float """
        h = int(hora)
        resto = hora - h
        m = int(resto * 60)
        resto_m = (resto * 60) - m
        s = int(resto_m * 60)

        # Los setters ya validan los rangos
        self.setHora(h)
        self.setMinuto(m)
        self.setSegundo(s)

    # SETTERS
    def setHora(self, hora):
        """Setter para hora con validación"""
        if 0 <= hora <= 24:
            self.__hora = hora
        else:
            self.__hora = 0

    def setMinuto(self, minuto):
        """Setter para minuto con validación"""
        if 0 <= minuto <= 59:
            self.__minuto = minuto
        else:
            self.__minuto = 0

    def setSegundo(self, segundo):
        """Setter para segundo con validación"""
        if 0 <= segundo <= 59:
            self.__segundo = segundo
        else:
            self.__segundo = 0

    # GETTERS
    def getHora(self):
        """Getter para hora"""
        return self.__hora

    def getMinuto(self):
        """Getter para minuto"""
        return self.__minuto

    def getSegundo(self):
        """Getter para segundo"""
        return self.__segundo

    # MÉTODOS DE INCREMENTO
    def incrementar_segundos(self, segundos):
        """
        Incrementa segundos a la hora, convirtiendo automáticamente a minutos/horas

        :param segundos: segundos a aumentar
        """
        total_segundos = self.getSegundo() + segundos

        minutos_extra = total_segundos // 60
        segundos_finales = total_segundos % 60

        self.setSegundo(segundos_finales)

        if minutos_extra > 0:
            self.incrementar_minutos(minutos_extra)

    def incrementar_minutos(self, minutos):
        """
        Incrementa minutos a la hora, convirtiendo automáticamente a horas

        :param minutos: minutos a aumentar
        """
        total_minutos = self.getMinuto() + minutos

        horas_extra = total_minutos // 60
        minutos_finales = total_minutos % 60

        self.setMinuto(minutos_finales)

        if horas_extra > 0:
            self.incrementar_horas(horas_extra)

    def incrementar_horas(self, horas):
        """
        Incrementa horas con ciclo de 24 horas

        :param horas: horas a aumentar
        """
        total_horas = self.getHora() + horas
        horas_finales = total_horas % 24
        self.setHora(horas_finales)

    def __str__(self):
        """Retorna la hora en formato HH:MM:SS"""
        return f"{self.getHora():02d}:{self.getMinuto():02d}:{self.getSegundo():02d}"

    # ENCAPSULACIÓN EN PYTHON (Properties)
    hora = property(getHora, setHora)
    minuto = property(getMinuto, setMinuto)
    segundo = property(getSegundo, setSegundo)
