"""
TIPOS DE COLECCIONES DE PYTHON
"""

l = [10,20,[30,"Treinta","XXXX"], 40, 50] #lista
t = (10,20,30,40,50,60,70,80,90,100) #tupla

print(l[2][1])
#acceder a un elemento de una lista dentro de otra lista

print(l[-3])
#acceder a un elemento de una lista desde el final

print(t[0])
#acceder a un elemento de una tupla

print(t[1:4])
#acceder a un rango de elementos de una tupla

print(t[1:9:2])
#acceder a un rango de elementos de una tupla con saltos (de dos en dos)

print(t[::-1])
#reversa

print(t[:10:3])
#acceder a un rango de elementos de una tupla con saltos (de tres en tres)

print(t[1:8:])
#acceder a un rango de elementos de una tupla sin saltos desde el elemento 1 al 7 en exclusivo

print(t[::])
#acceder a todos los elementos de una tupla

l[4] = "Cincuenta"
print(l)
#las listas son mutables, se pueden cambiar sus valores
#las tuplas son inmutables, no se pueden cambiar sus valores
t[4] = "Cincuenta"
print(t)

