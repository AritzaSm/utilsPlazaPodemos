#!/usr/bin/python
# PlazaPodemos, Creacion de multiples sub-reddits a partir de lista desde archivo
# soportevotaciones@podemos.info
# Aritza, 16/10/2014
# -*- coding: utf-8 -*-

import praw
import time
import unicodedata
import os


def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

# Datos para la etiqueta
subReddit=''

prefijo ='PlazaPodemos'
prefijo2 = 'Plaza'

prefijoLargo = u'Plaza Podemos de '
descripcion = u'podemos!'

nombreCorto = ''
nombreLargo = ''

# Contrasenas
adminUser = 'PlazaPodemos'
adminPass = ''



# Definiciones para el arichivo 
fLista = 'municipiosParcial.txt'
lista = []

# Algunos contadores
numOk = 0
numError=0

# Cargamos los datos
os.system('clear')
print('Podemos!')

r = praw.Reddit(user_agent='FlairBotPodemos')
r.login( adminUser, adminPass )

with open(fLista) as f:
	lista = f.read().splitlines()


print('La lista de las Plazas....')

for w in lista:
	try:
		
		nombreCorto = prefijo + strip_accents ( w.decode('utf-8').replace(' ','') )
		nombreLargo = prefijoLargo + strip_accents( w.decode('utf-8') )
		
		os.system('clear')
		print 'Creando: ' + nombreCorto
		print 'Nombre Largo: ' + nombreLargo
		
		print (' La creo? (s/n) ')
		respuesta = raw_input()

		if respuesta == "s" : 
			print 'Creando...'
			r.create_subreddit( nombreCorto, nombreLargo, language='es',subreddit_type='private', content_options='any', over_18=False, show_media=True )

	except praw.errors.InvalidSubreddit:
		print 'Error: en el subReddit: ',w,
		numError = numError + 1
	else:
		numOk = numOk + 1

# Presenta algunos resultados:
print "Asignaciones con exito:", numOk
print "Asignaciones erroneas:", numError				
