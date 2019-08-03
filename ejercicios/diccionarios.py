#!/usr/bin/python
#!-*- encoding: utf-8 -*-


familia = {
	'jose': {
				'edad': '41',
				'hijos': 'No'				
	},
	'miguel': {
				'edad': '40',
				'hijos': 'Si'
	},
	'yessenia': {
				'edad': '34',
				'hijos': 'Si'
	},
	'jaime': {
				'edad': '30',
				'hijos': 'Si'
	},
	'uriel': {
				'edad': '27',
				'hijos': 'No',
	},
	'lalo': {
				'edad': '24',
				'hijos': 'Si'
	}
}

familia['gerardo']={'edad':'51', 'hijos':'no'}

##print(familia)

for k, v in familia.items():
	print("Nombre:", k.title(), "Edad:", v['edad'], ' Hijos: ', v['hijos'])