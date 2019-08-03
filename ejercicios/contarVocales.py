#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales. Se puede hacer que el usuario sea quien elija la palabra.

#!/usr/bin/env python
#-*- coding utf-8 -*-

def contarVocales(palabra):
	countA=0
	countE=0
	countI=0
	countO=0
	countU=0
	dicc = {}
	for i in palabra:		
		if(i.upper() == "A"):
			countA+=1
		elif(i.upper()=="E"):
			countE+=1
		elif(i.upper()=="I"):
			countI+=1
		elif(i.upper()=="O"):
			countO+=1
		elif(i.upper()=="U"):
			countU+=1

	dicc={
		'A': countA,
		'E': countE,
		'I': countI,
		'O': countO,
		'U': countU
	}

	return dicc





print("---CONTAR VOCALES---")
print("\n\n")

print("Introduzca la palabra y te diré cuántas vocales hay: ")
palabra = input()

respuesta = contarVocales(palabra)

for i in respuesta.items():
	print(i)