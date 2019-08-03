#!/usr/bin/env python
#-*- encoding: utf-8 -*-

cadena = "oso"
print(cadena[0])
aux = ""

for i in range(len(cadena)-1, -1, -1):	
	aux+=cadena[i]
	

if cadena == aux:
	print("La frase \'{}\' ES palindromo".format(cadena))
else:
	print("La frase \'{}\' NO ES palindromo".format(cadena))