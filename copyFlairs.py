#!/usr/bin/python
# PlazaPodemos, copia asignaciones de etiquetas a plazas 
# Hay que editar los valores iniciales para que los use en la asignacion
# Aritza, 8/2/2015
# -*- coding: utf-8 -*-

import praw
import time
import argparse

# Valores iniciales 
adminUser = ''
adminPass = ''
plazaOrigen = ''
plazaDestino = ''
numOk=0
numError=0

# Opciones de linea de comandos
parser = argparse.ArgumentParser(description='Copiamos etiquetas de una plaza a otra')


parser.add_argument('-o','--origen', default='podemos', help='Plaza origen, de donde lee las etiquetas')
parser.add_argument('-d','--destino', help='Plaza destieno, donde meten las etiquetas')
parser.add_argument('-u','--user', help='especifica un usuario moderador')
parser.add_argument('-p','--password', help='contrasena del moderador')
parser.add_argument('-e','--etiqueta', help='Clase CSS de la etiqueta que moveremos')
args = parser.parse_args()

if args.destino and args.etiqueta:

	print 'Podemos!'
	#Inicializamos las varianles. 

	plazaOrigen = args.origen
	plazaDestino = args.destino
	adminUser = args.user
	adminPass = args.password
	distintivo = args.etiqueta


# Cargamos los datos

	print 'recogiendo distintivos de ', plazaOrigen

	r = praw.Reddit(user_agent='FlairBotPodemos')
	r.login(adminUser, adminPass)

	listaDistintivos = r.get_subreddit(plazaOrigen).get_flair_list(limit=None)

	flairMap = []

	for i in listaDistintivos:
		if i['flair_css_class'] == distintivo:
			flairMap.append(i)
			numOk = numOk + 1
	r.get_subreddit(plazaDestino).set_flair_csv(flairMap)
	
	print 'Hecho ;)'
	print "Asignaciones con exito:", numOk
	print "Asignaciones erroneas:", numError				
else:
	print 'Error: falta algun parametro'
