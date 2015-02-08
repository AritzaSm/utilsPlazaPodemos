#!/usr/bin/python
# PlazaPodemos, copia la imagenes de una plaza a otra 
# Hay que editar los valores iniciales para que los use en la asignacion
# Aritza, 8/2/2015
# -*- coding: utf-8 -*-

import praw
import argparse
import urllib
import os

# Contrasenas
adminUser = ''
adminPass = ''

# Valores iniciales 
plazaOrigen = ''
plazaDestino = ''
imgDir ='images/'

# Un par de funciones para tratar la cache de imagenes
def CargaImagenes():
	for img in images:
		filepath = imgDir + img['name']+'.png'
		if not os.path.isfile(filepath):
			urllib.urlretrieve(img['url'], filepath)

def BorraCache():
	for img in images:
		filepath = imgDir + img['name']+'.png'
		if os.path.isfile(filepath):
			os.remove(filepath)


# Opciones
parser = argparse.ArgumentParser(description='Copiamos las imagnes de una plaza a otra')
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
	images = r.get_stylesheet(plazaOrigen)['images']

	print 'Bajando las imagenes de',plazaOrigen
	CargaImagenes()
	print 'Subiendo las imagenes para: ', plazaDestino
	for img in images:
		filepath = imgDir + img['name'] + '.png'
		print 'Subiendo imagen: ',filepath
		r.upload_image(plazaDestino,filepath,name=img['name'],header=False)
	
	BorraCache()
	print 'Hecho!'

else:
	print ('Error: faltan argumentos')





