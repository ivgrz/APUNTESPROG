# ==============================================
# DEMOSTRACIÓN DE MÉTODOS DE LISTAS Y CADENAS
# ==============================================

# Lista inicial de colores
colores = ["rojo", "verde", "azul"]
print("Lista inicial:", colores)

# 1. append() -> añadir un elemento al final
colores.append("amarillo")
print("Después de append:", colores)

# 2. insert() -> insertar en una posición concreta
colores.insert(1, "negro")
print("Después de insert en posición 1:", colores)

# 3. extend() -> añadir todos los elementos de otra lista
colores.extend(["blanco", "gris"])
print("Después de extend:", colores)

# 4. remove() -> eliminar un elemento por nombre
colores.remove("negro")
print("Después de remove('negro'):", colores)

# 5. pop() -> elimina y devuelve el elemento en un índice
eliminado = colores.pop(2)
print("Después de pop(2), eliminó:", eliminado, "->", colores)

# 6. index() -> posición de un elemento
pos = colores.index("amarillo")
print("El índice de 'amarillo' es:", pos)

# 7. count() -> cuántas veces aparece un elemento
repetidos = colores.count("rojo")
print("Cantidad de veces que aparece 'rojo':", repetidos)

# 8. sort() -> ordenar alfabéticamente
colores.sort()
print("Lista ordenada:", colores)

# 9. reverse() -> invertir el orden
colores.reverse()
print("Lista invertida:", colores)

# 10. len(), max(), min()
print("Longitud de la lista:", len(colores))
print("Elemento mayor (alfabético):", max(colores))
print("Elemento menor (alfabético):", min(colores))

# 11. join() -> unir lista en un string
cadena_colores = ", ".join(colores)
print("Colores unidos con join:", cadena_colores)

# 12. find() -> buscar un substring dentro del string
print("find('azul') ->", cadena_colores.find("azul"))   # -1 si no está
print("find('rojo') ->", cadena_colores.find("rojo"))

# 13. split() -> separar un string en lista
lista_split = cadena_colores.split(", ")  # se separa por coma y espacio
print("split(', ') ->", lista_split)

# 14. replace() -> reemplazar un substring por otro
cadena_replace = cadena_colores.replace("rojo", "ROJO")
print("replace('rojo','ROJO') ->", cadena_replace)

# 15. partition() -> divide en 3 partes (antes, separador, después)
particion = cadena_colores.partition("gris")
print("partition('gris') ->", particion)

# 16. clear() -> vaciar la lista
colores.clear()
print("Después de clear:", colores)

