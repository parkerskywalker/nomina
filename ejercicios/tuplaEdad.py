#Ejercicio 7
#Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20. Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

#!/usr/bin/env python
#-*- coding utf-8 -*-

edades=(1,2,3,4,5,6,7,8,9,20,)

def contadorEdades(edad):

	print(edad)
	
	for i in edad:		
		count=0
		
		if int(i) >= 20:
			count+=1

	return count


print("Personas con edad superiores a 20 son: ", contadorEdades(edades))
