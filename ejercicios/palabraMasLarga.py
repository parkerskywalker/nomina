#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 

#!/usr/bin/env python
#-*- coding utf-8 -*-

lista=["Una frase", "Esta frase es la mas larga de todas", "corta", "una mas", "una menos dos"]

def mas_larga(lista):
	
	temp=0
	maslarga=""
	
	for i in lista:
		if len(i) > temp:
			maslarga=i
			temp = len(i)

	return maslarga



print("---PALABRA MAS LARGA---")

respuesta=mas_larga(lista)


print("La frase más larga de la lista tiene es: \n", respuesta)
