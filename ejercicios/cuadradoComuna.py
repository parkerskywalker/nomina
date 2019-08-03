#!/usr/bin/env python
#!-*- encoding:utf-8 -*-

dato = int(input("Ingrese el num del lado: "))

#linea arriba
for c in range(dato+1):
	print("* ", end="")	

print()

j=1
x=1
y=1
while j <= dato-2:	
	for k in range(dato):		
		if k == 0:
			print("* ", end=" ")
		elif k == dato-1:
			print(" *", end=" ")
		elif j == x and k == y:
			print("*", end=" ")
			x+=1
			y+=1
		elif dato-k == j+1:
			print("*", end=" ")
		else:
			print(" ", end=" ")	

	print()
	j+=1


i=0
while i < dato+1:
	print("* ", end="")
	i+=1

