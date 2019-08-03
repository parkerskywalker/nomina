#Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

#!/usr/bin/env python
#-*- coding utf-8 -*-

print("--- AÑO BISIESTO --- \n")


def bisiesto(anio):

	if(int(anio)%4==0 and int(anio)%400==0):
		return "Es bisiesto"
	else:
		return "No es bisiesto"


print("Introduzca el año: ")
anio = input()

respuesta = bisiesto(anio)

print(respuesta)