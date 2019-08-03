#Ejercicio 6
#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

#!/usr/bin/env python
#-*- coding utf-8 -*-

context={}
lista=[]

print("---PEQUEÑO PROGRAMITA---")
print("\n\n")

print("Ingrese el año en curso: ")
anio = input()

for i in range(3):
	print("Ingrese el nombre:")
	nom = input()
	print("Ingrese el año de nacimiento:")
	edad = input()

	cumpliran = int(anio) - int(edad)

	context = {
		'nom':nom,
		'anio': anio,
		'edad': cumpliran
	}
	lista.append(context)


for i in lista:
	print(i)

