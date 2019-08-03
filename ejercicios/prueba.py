#!/usr/bin/env python
#!-*- encoding:utf-8 -*-


dato = 10

dato = 10

n=0
x=1
y=1

for r in range(1, dato, 1):	
	#print("*", end="")	
	for c in range(1, dato, 1):		
		print(" ", end="")		
		if r == x and c == y:			
			print("*", end="")
			#print(r,c, end="")
			x+=1
			y+=1

	print()





""" NO FUNCIONA
for rr in range(1, dato, 1):
	for cc in range(1, dato, 1):
		#print(rr, cc, end="")
		#print("rr={} cc={} d={}".format(rr, cc, cc-xx), end="")
		d=cc-xx
		#print("rr"+str(rr) + "cc"+str(cc) + "|d="+str(d), end="")
		
		
		if cc == d:
			print(" ", end="")
			xx-=1
			yy+=1
		else:
			print("*", end="")
		
	print()
"""