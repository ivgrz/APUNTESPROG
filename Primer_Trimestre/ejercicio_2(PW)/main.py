from Hora import Hora

if __name__ == "__main__":
    print("=== PRUEBAS DE CREACIÓN DE OBJETOS HORA ===\n")

    # Prueba 1: Con enteros
    print("1. Creación con enteros: Hora(10, 30, 45)")
    hora1 = Hora(10, 30, 45)
    print(f"   Resultado: {hora1}")
    print(f"   Repr: {repr(hora1)}\n")

    # Prueba 2: Con string
    print("2. Creación con string: Hora('23:59:50')")
    hora2 = Hora("23:59:50")
    print(f"   Resultado: {hora2}\n")

    # Prueba 3: Con float
    print("3. Creación con float: Hora(14.575)")
    hora3 = Hora(14.575)
    print(f"   Resultado: {hora3}")
    print(f"   (14.575 horas = 14h + 0.575*60min = 14h 34.5min = 14:34:30)\n")

    # Prueba 4: Con lista
    print("4. Creación con lista: Hora([8, 15, 30])")
    hora5 = Hora([8, 15, 30])
    print(f"   Resultado: {hora5}\n")

    # Prueba 5: Validación de valores inválidos
    print("5. Validación con valores inválidos: Hora(25, 61, 70)")
    hora4 = Hora(25, 61, 70)
    print(f"   Resultado: {hora4}")
    print(f"   (Valores fuera de rango se convierten a 0)\n")

    print("=" * 50)
    print("\n=== PRUEBAS DE INCREMENTO ===\n")

    # Prueba 6: Incremento de horas
    print(f"6. Incremento de horas")
    print(f"   Hora antes: {hora1}")
    hora1.incrementar_horas(2)
    print(f"   Después de incrementar 2 horas: {hora1}\n")

    # Prueba 7: Incremento de minutos con overflow
    print(f"7. Incremento de minutos con overflow")
    print(f"   Hora antes: {hora1}")
    hora1.incrementar_minutos(130)  # 130 min = 2h 10min
    print(f"   Después de incrementar 130 minutos: {hora1}\n")

    # Prueba 8: Incremento de segundos con overflow múltiple
    print(f"8. Incremento de segundos (cruza medianoche)")
    hora2_copia = Hora("23:59:50")
    print(f"   Hora antes: {hora2_copia}")
    hora2_copia.incrementar_segundos(20)
    print(f"   Después de incrementar 20 segundos: {hora2_copia}")
    print(f"   (Cruzó la medianoche correctamente)\n")

    print("=" * 50)
    print("\n=== PRUEBAS DE PROPERTIES ===\n")

    # Prueba 9: Uso de properties
    print("9. Acceso mediante properties")
    hora6 = Hora(15, 45, 30)
    print(f"   hora6.hora = {hora6.hora}")
    print(f"   hora6.minuto = {hora6.minuto}")
    print(f"   hora6.segundo = {hora6.segundo}\n")

    print("10. Modificación mediante properties")
    hora6.hora = 18
    hora6.minuto = 20
    hora6.segundo = 15
    print(f"   Después de modificar: {hora6}\n")

    print("=" * 50)
    print("\n=== PRUEBAS DE COMPARACIÓN ===\n")

    # Prueba 11: Comparación
    h1 = Hora(10, 30, 0)
    h2 = Hora(10, 30, 0)
    h3 = Hora(15, 0, 0)

    print(f"11. Comparaciones:")
    print(f"   {h1} == {h2}: {h1 == h2}")
    print(f"   {h1} == {h3}: {h1 == h3}")
    print(f"   {h1} < {h3}: {h1 < h3}")
    print(f"   {h3} < {h1}: {h3 < h1}")
