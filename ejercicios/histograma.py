#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#******

#!/usr/bin/env python
#-*- coding utf-8 -*-
lista = [4,9,7]

def procedimiento(list):	
	#for i in list:		
	#	var = ""		
	#	for x in range(0,i):			
	#		var+="*"

	#	print(var)

	for i in list:
		print(i*"x")


print("Pinta histograma")
procedimiento(lista)