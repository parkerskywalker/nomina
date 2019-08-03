#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.


#!/usr/bin/env python
#-*- coding utf-8 -*-
lista = [91,4,5,6,2,55]


def max_in_list(lista):	
	temp=0
	for i in lista:		
		if i > temp:
			temp=i

	return temp




print("--------MAXIMO DE UNA LISTA-----------------\n\n")
respuesta = max_in_list(lista)

print("El maximo de la lista es: ", respuesta)
