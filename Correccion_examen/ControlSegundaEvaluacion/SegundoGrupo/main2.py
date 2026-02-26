from TorneoXestor2 import Torneo_Gestor
from Torneo2 import Torneo2

if __name__ == '__main__':
    # gestor = Torneo_Gestor()
    # gestor.bucle_principal()
    # FIX: Torneo2 requiere 'nome' como argumento obligatorio (antes se llamaba sin argumentos)
    torneo = Torneo2("Torneo4aXornada")
    # FIX: movido dentro del bloque if __name__ (antes estaba fuera y se ejecutaba siempre al importar)
    # torneo.importar_resultados_fichero2(
    # '/Users/vnangz/Library/CloudStorage/GoogleDrive-ivangxz1403@gmail.com/Mi unidad/APUNTESPROG/Correccion_examen/ControlSegundaEvaluacion/SegundoGrupo/resultados4xornada.csv')
    torneo.importar_resultados_csv_diccionario(
        '/Users/vnangz/Library/CloudStorage/GoogleDrive-ivangxz1403@gmail.com/Mi unidad/APUNTESPROG/Correccion_examen/ControlSegundaEvaluacion/SegundoGrupo/resultados4xornada.csv')
