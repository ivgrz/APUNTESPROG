# Si quieres importar un diccionario desde otro archivo llamado colores.py,
# no deberías volver a definirlo aquí. Para esta versión lo dejo definido.

colores = {
    "Verde": "green",
    "rojo": "red",
    "amarillo": "yellow",  # corregido
    "azul": "blue"
}

# Usamos get() para evitar error si la clave no existe
print(colores.get("vermello", "La clave 'vermello' no existe"))

# Mostrar la traducción de "rojo"
print(colores["rojo"])

# Mostrar solo los valores (traducciones)
for color in colores.values():
    print(color)

# Mostrar solo las claves (colores en español)
for clave in colores.keys():
    print(clave)


colores.pop("Verde")

print(colores.items())

