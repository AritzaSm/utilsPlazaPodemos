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
plazaOrigen = ''
plazaDestino = ''
numOk = 0

# Opciones
parser = argparse.ArgumentParser(description='Copiamos un css de una plaza a otra')


parser.add_argument('-o','--origen', default='podemos', help='Plaza origen, de donde lee el CSS')
parser.add_argument('-d','--destino', help='Plaza destieno, donde sube el css. Tambien admite lista separada por comas')
parser.add_argument('-u','--user', help='especifica un usuario moderador')
parser.add_argument('-p','--password', help='contrasena del moderador')
args = parser.parse_args()

if args.destino:

	print 'Podemos!'
	#Inicializamos las varianles. 

	plazaOrigen = args.origen
	plazas = args.destino.split(',')
	adminUser = args.user
	adminPass = args.password


	# Cargamos los datos
	r = praw.Reddit(user_agent='PlazaPodemosBot')
	r.login( adminUser, adminPass )
	r.config.decode_html_entities = True
	estilo = r.get_stylesheet(plazaOrigen)['stylesheet']

	for plazaDestino in plazas:
		print 'Estableciendo estilo en', plazaDestino
		try:
			r.set_stylesheet(plazaDestino, estilo)
		except requests.exceptions.ReadTimeout:
			print 'Vaya, parece que reddit no responde, espero 1 minuto ...'
			time.sleep(60)
			pass

		numOk = numOk + 1
	
	print'Hecho ; )'
	print numOk,'Plazas actualizadas'	

else:
	print ('Error: faltan argumentos')





