abecedario = ["a", "b", "c", "d", "e", "f", "g",
              "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]



print (len(abecedario))
abecedario.append ('d') #añade d al final
print(abecedario)
abecedario.extend(['e', 'f', 'g']) #añade una lista de elementos al final
print(abecedario)
abecedario.insert(2, 'h')  #inserta una letra en una posicion exacta
print(abecedario)

abecedario.remove('a') #elimina
print(abecedario)
print (abecedario.pop()) #elimina lo ultimo de la lista abecedario
print(abecedario)

abecedario.count ("e") #cuenta todas las e de esta lista

abecedario.reverse()
print(abecedario)

mensaje = "Hola, Pulab!"
slicing = mensaje[2:6]
print(slicing)