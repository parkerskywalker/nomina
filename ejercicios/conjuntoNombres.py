#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)


nombres=["Andrea", "Alberto", "Roberto", "Lucia", "Sandra", "Juan", "aicardo"]

def buscarLetra(busca, nombres):
	count=0
	for i in nombres:		
		#if busca in i:
			#count+=1
		for x in i:
			print(x)
			if x[0]==busca:
				count+=1

			break

	return count


print("--- BUSCA LETRA EN UNA LISTA ---")
print("Introduzca una letra a buscar: ")
busca = input()

respuesta = buscarLetra(busca, nombres)

print("La respuesta es: ", respuesta, "veces aparece la letra: ", busca, " en la lista de nombres.")