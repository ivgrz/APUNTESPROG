"""
Hacer una funcion que elmine los espacios en blanco al inicio y al final de una cadena de texto.
Pero deje los espacios en blanco que haya entre palabras.
Sin usar trim() ni strip().
"""
def eliminar_espacios_final_inicio(cadena):
    inicio = 0
    fin = len(cadena) - 1

    # Avanza mientras haya espacios

    while inicio <= fin and cadena[inicio] == " ": #El while se detiene al encontrar una letra
        inicio += 1

    # Retrocede mientras haya espacios

    while fin >= inicio and cadena[fin] == " ": #El while se detiene al encontrar una letra
        fin -= 1

    # Devolvemos el texto sin espacios en los extremos

    return cadena[inicio:fin+1]

print(eliminar_espacios_final_inicio("  una cadena cualquiera  "))