from persona import Persona


class Alumno(Persona):
    contador_alumnos = 0

    def __init__(self, nombre, edad, dni, direccion, nacionalidad, fecha_nacimiento, ciclo):
        super().__init__(nombre, edad, dni, direccion, nacionalidad, fecha_nacimiento)
        self.ciclo = ciclo

        Alumno.contador_alumnos += 1

    @classmethod
    def contar_alumnos(cls, lista_alumnos=None):
        """
        Cuenta alumnos. Si se pasa una lista, cuenta esa lista.
        Si no, retorna el total de alumnos creados.
        """
        if lista_alumnos is None:
            return cls.contador_alumnos
        return len(lista_alumnos)

    def __str__(self):
        """Representación en string del alumno"""
        return f"{super().__str__()}\nCiclo: {self.ciclo}"
