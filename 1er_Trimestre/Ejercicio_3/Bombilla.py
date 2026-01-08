class Bombilla:
    """Clase que representa una bombilla con interruptor individual y general"""
    interruptor_general = False  # Se llama atributo de clase o atributo estático

    def __init__(self, color, numero_serie):
        """
        Constructor de la bombilla

        :param color: Color de la bombilla
        :param numero_serie: Número de serie único de la bombilla
        """
        self.__encendida = False
        self.setcolor(color)
        self.setnumero_serie(numero_serie)

    @classmethod  # Sirve para definir métodos que afectan a la clase en sí, no a instancias individuales
    def cambiar_interruptor_general(cls, estado):
        """
        Cambia el estado del interruptor general para todas las bombillas

        :param estado: True para encender, False para apagar
        """
        cls.interruptor_general = estado

    @classmethod
    def obtener_interruptor_general(cls):
        """
        Obtiene el estado del interruptor general

        :return: True si está encendido, False si está apagado
        """
        return cls.interruptor_general

    # GETTERS Y SETTERS

    def getcolor(self):
        """Obtiene el color de la bombilla"""
        return self.__color

    def setcolor(self, color):
        """Establece el color de la bombilla"""
        self.__color = color

    def getnumero_serie(self):
        """Obtiene el número de serie de la bombilla"""
        return self.__numero_serie

    def setnumero_serie(self, numero_serie):
        """Establece el número de serie de la bombilla"""
        self.__numero_serie = numero_serie

    # MÉTODOS DE CONTROL
    def conmuta(self):
        """Cambia el estado de la bombilla (encendida/apagada)"""
        self.__encendida = not self.__encendida

    def enciende(self):
        """Enciende la bombilla"""
        self.__encendida = True

    def apaga(self):
        """Apaga la bombilla"""
        self.__encendida = False

    def estado(self):
        """Retorna el estado de la bombilla como string"""
        return "encendida" if self.__encendida else "apagada"

    def esta_encendida(self):
        """
        Comprueba si la bombilla está realmente encendida
        (requiere que tanto la bombilla como el interruptor general estén encendidos)

        :return: True si ambos están encendidos, False en caso contrario
        """
        return self.__encendida and self.interruptor_general

    def __str__(self):
        """Representación en string de la bombilla"""
        return (f"La bombilla de color {self.getcolor()}\n"
                f"Numero de serie: {self.getnumero_serie()}\n"
                f"esta {self.estado()}"
                f" y el interruptor general esta {'encendido' if Bombilla.interruptor_general else 'apagado'}.\n")
