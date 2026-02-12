def ordenar_lista(lista):
	laux = lista[:]
	lord = []

	while (len(laux) > 1):
		ind_max = 0
		for i in range(len(laux)-1):
			if laux[ind_max]<laux[i+1]: # Comparamos el primer elemento con el siguiente, si el siguiente es mayor, se convierte en el nuevo máximo
				ind_max = i+1
		lord.append(laux.pop(ind_max)) # Agregamos el máximo a la lista ordenada y lo eliminamos de la lista auxiliar
	lord.append(laux[0]) # Agregamos el último elemento restante a la lista ordenada
	return lord

lo = ordenar_lista([1,4,6,2,1,8,5,4])
print(lo)

