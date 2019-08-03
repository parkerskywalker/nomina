#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".


def generar_n_caracteres(num):	
	return 'x'*int(num)



print("Introduzca el núm de veces: ")
numC = input()
resultado = generar_n_caracteres(numC)

print("Resultado: ", resultado)