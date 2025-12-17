from Cliente import Cliente
from Llamada_Telefonica import Llamada
from Distintas_Llamadas import distinta_llamada

if __name__ == '__main__':
    # 1. Crear cliente
    c1 = Cliente("Juan", "Y8798454", "36320", "34625844235")

    # 2. Crear el gestor
    gestor = distinta_llamada()

    # 3. Registrar una llamada saliente de 10 minutos
    ll1 = Llamada(c1, "12345", "12:00:00", "12:10:00", saliente=True)
    gestor.anhadir_llamada(ll1)

    # 4. Resultados
    print(c1)
    print(gestor)
    print(f"Total a pagar por el cliente {c1.dni}: {gestor.importe(c1.dni)}€")