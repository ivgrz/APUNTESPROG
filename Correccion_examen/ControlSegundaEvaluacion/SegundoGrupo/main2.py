from TorneoXestor2 import Torneo_Gestor
from Torneo2 import Torneo2
from equipo2 import Equipo

if __name__ == '__main__':
    # Crear equipos manualmente según los datos del CSV
    celta    = Equipo("Celta",   ganhados=1, perdidos=0, empates=0)
    sevilla  = Equipo("Sevilla", ganhados=0, perdidos=1, empates=0)
    espanol  = Equipo("Español", ganhados=0, perdidos=1, empates=0)
    girona   = Equipo("Girona",  ganhados=1, perdidos=0, empates=0)
    betis    = Equipo("Betis",   ganhados=0, perdidos=1, empates=0)
    villareal = Equipo("Villareal", ganhados=1, perdidos=0, empates=0)

    torneo = Torneo2("Torneo4aXornada")
    torneo.add_equipo(celta)
    torneo.add_equipo(sevilla)
    torneo.add_equipo(espanol)
    torneo.add_equipo(girona)
    torneo.add_equipo(betis)
    torneo.add_equipo(villareal)

    # Exportar clasificacion ordenada por puntos al fichero CSV
    import os
    ruta_clasificacion = os.path.join(os.path.dirname(__file__), "clasificacion.csv")
    torneo.importar_resultados_clasificacion_csv(nomefich=ruta_clasificacion)
    print("Clasificacion exportada a 'clasificacion'")
