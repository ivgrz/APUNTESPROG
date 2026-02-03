# Un Set (conjunto) en Python es una colección desordenada de elementos únicos.
# Sus principales características son:
# 1. No permite duplicados: si añades un elemento que ya existe, no sucede nada.
# 2. Es desordenado: los elementos no tienen un índice o posición fija.
# 3. Elementos inmutables: los elementos del set deben ser de tipos que no cambien (como strings, números o tuplas).

# Crear un set con elementos
frutas = {"manzana", "banana", "cereza"}

# add(): Añadir un elemento
frutas.add("naranja")

# update(): Añadir múltiples elementos (pueden ser listas u otros sets)
frutas.update(["uva", "mango"])

# remove(): Elimina un elemento (lanza error si no existe)
frutas.remove("banana")

# discard(): Elimina un elemento (NO lanza error si el elemento no existe)
frutas.discard("pera")

print(frutas)

numeros_repetidos = [1, 2, 2, 3, 4, 4, 4, 5]

# Convertir la lista a set elimina los duplicados automáticamente
numeros_unicos = list(set(numeros_repetidos))

print(numeros_unicos) # Resultado: [1, 2, 3, 4, 5]

colores = {"rojo", "verde", "azul"}

# pop() - Quita uno al azar
eliminado = colores.pop()

# clear() - Vacía el set
colores.clear()

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {10, 20}

print(A.issubset(B))    # True (A está dentro de B)
print(B.issuperset(A))  # True (B contiene a A)
print(A.isdisjoint(C))  # True (No comparten nada)

mis_apps = {"WhatsApp", "Instagram", "TikTok"}
apps_productividad = {"WhatsApp", "Slack", "Notion"}

# Solo me quedo con las que sirven para trabajar
mis_apps.intersection_update(apps_productividad)

print(mis_apps) # Resultado: {'WhatsApp'}

programadores = {"Python", "Java", "C++", "JavaScript"}
analistas = {"Excel", "SQL", "Python", "PowerBI"}

# UNION (|): Todos los intereses (sin repetir Python)
todos = programadores | analistas
# {'Python', 'Java', 'C++', 'JavaScript', 'Excel', 'SQL', 'PowerBI'}

# INTERSECCIÓN (&): Solo lo que tienen en común
comun = programadores & analistas
# {'Python'}

# DIFERENCIA (-): Lo que tiene el primero que NO tiene el segundo
solo_programadores = programadores - analistas
# {'Java', 'C++', 'JavaScript'}

# DIFERENCIA SIMÉTRICA (^): Lo que NO comparten (excluye la intersección)
no_compartido = programadores ^ analistas
# {'Java', 'C++', 'JavaScript', 'Excel', 'SQL', 'PowerBI'}