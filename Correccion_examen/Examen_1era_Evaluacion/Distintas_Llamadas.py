from Llamada_Telefonica import Llamada


class distinta_llamada:
    def __init__(self):
        self.lista_llamadas = []

    def anhadir_llamada(self, llamada: Llamada):
        self.lista_llamadas.append(llamada)

    def importe(self, dni_buscado):
        total = 0.0
        precio_minuto = 0.15  # Tarifa fija por minuto

        for ll in self.lista_llamadas:
            # Comparamos el DNI del cliente de la llamada
            if ll.get_cliente().getdni() == dni_buscado:
                # Solo se facturan las llamadas salientes
                if ll.get_saliente():
                    total += ll.duracion() * precio_minuto
        return round(total, 2)

    def __str__(self):
        res = "--- HISTORIAL DE LLAMADAS ---\n"
        for ll in self.lista_llamadas:
            tipo = "Saliente" if ll.get_saliente() else "Entrante"
            res += f"Destino: {ll.telefono_i} | Tipo: {tipo} | Duración: {ll.duracion()} min\n"
        return res