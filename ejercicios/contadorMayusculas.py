#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

#!/usr/bin/env python
#-*- coding utf-8 -*-

def contMayus(chain):
	count=0
	for i in chain:		
		if(i.isupper()):			
			count+=1

	return count

print("Por favor, introduzca algun texto: ")
chain = input()
respuesta = contMayus(chain)

print("La cadena tiene:", respuesta, " mayusculas.")