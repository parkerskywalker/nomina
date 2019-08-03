#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres. 


#!/usr/bin/env python
#-*- coding utf-8 -*-
lista=["Una", "dostres", "cuatrocincoseis", "sieteochonuevediez", "una frase mas larga que otras"]


def filtrar_palabras(num, list):	
	dato=0
	temp=[]
	for i in lista:		
		dato=len(i)

		if(dato > int(num)):
			temp.append(i)
		
	return temp



print("--- FILTRAR PALABRAS ---")
print("\n\n")
print("Deme un numero:")
entrada = input()

respuesta = filtrar_palabras(entrada, lista)

print(respuesta)
