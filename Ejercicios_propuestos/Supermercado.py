"""
Hacer una simulacion de caja de supermercado.
Debe contener:
- Calculo de importe por caja
- Calculo de importe total
- Impresion contenido caja
- Impresion contenido total
-
"""
def supermercado():

    efectivo = [[1,[50,13],[20,5],[10,5],[5,3],[1,10]],
                [2,[50,2],[20,9],[10,6],[0.20,3],[0.05,23]],
                [3,[100,1],[50,1],[10,2],[5,1],[1,5]]]
    importe_total = 0
    contenido_consolidado = {}
# Iteramos en la caja
    for caja in efectivo:
        numero_caja = caja[0]
        contenido_caja = caja[1:]
        importe_caja = 0
        # Calculamos el importe total por cada caja
        for valor, cantidad in contenido_caja:
            importe_caja += valor * cantidad
            valor_denominacion = valor
            contenido_consolidado[valor_denominacion] = contenido_consolidado.get(valor_denominacion, 0) + cantidad

        # Acumulamos el importe total
        importe_total += importe_caja

        print(f"\n El contenido de la caja {numero_caja} es: ")
        for valor, cantidad in contenido_caja:
            unidad_texto = "unidad" if cantidad == 1 else "unidades"
            print(f"- {cantidad} {unidad_texto} de ${valor:.2f} = ${valor*cantidad:.2f}")

        print(f"\n Importe de la caja {numero_caja}: {importe_caja:.2f}")
        print("-"*30)

# -----------------------------------------------------------------------------

    print(f"CONTENIDO TOTAL")
    print(f"Cantidad de billetes de cada denominacion: ")
# Obtenemos las denominaciones de menor a mayor

    denominaciones_ordenadas = sorted(contenido_consolidado.keys(), reverse=True)

    for valor in denominaciones_ordenadas:
        cantidad_total = contenido_consolidado[valor]
        total_monetario = valor * cantidad_total

        unidad_texto = "unidad" if cantidad_total == 1 else "unidades"
        print(f"- {cantidad_total} {unidad_texto} de ${valor:.2f} = ${total_monetario:.2f}")


# MUESTRA TOTAL DEL IMPORTE
    print(f"IMPORTE TOTAL: {importe_total:.2f}")


supermercado()


