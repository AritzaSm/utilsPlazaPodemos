#!/usr/bin/python
# PlazaPodemos, copia un css de una plaza a otra 
# Hay que editar los valores iniciales para que los use en la asignacion
# Aritza, 8/2/2015
# -*- coding: utf-8 -*-

import praw
import argparse

# Contrasenas
adminUser = ''
adminPass = ''

# Valores iniciales 
plazaOrigen = 'podemos'
plazaDestino = ''

# Opciones
parser = argparse.ArgumentParser(description='Copiamos un css de una plaza a otra')


parser.add_argument('-o','--origen', default='podemos', help='Plaza origen, de donde lee el CSS')
parser.add_argument('-d','--destino', help='Plaza destieno, donde mete el CSS')
parser.add_argument('-u','--user', help='especifica un usuario moderador')
parser.add_argument('-p','--password', help='contrasena del moderador')
args = parser.parse_args()

if args.destino:

	print 'Podemos!'
	#Inicializamos las varianles. 

	plazaOrigen = args.origen
	plazaDestino = args.destino
	adminUser = args.user
	adminPass = args.password

	# Cargamos los datos
	r = praw.Reddit(user_agent='PlazaPodemosBot')
	r.login( adminUser, adminPass )
	r.config.decode_html_entities = True

	print 'Estableciendo estilo en', plazaDestino
	estilo = r.get_stylesheet(plazaOrigen)['stylesheet']
	r.set_stylesheet(plazaDestino, estilo)
	print'Hecho ; )'
	

else:
	print ('Error: faltan argumentos')





