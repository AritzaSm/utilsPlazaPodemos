#!/usr/bin/python
# utilCSSb:
# 	Recorrer una lista de subs, recogida de un archivo y actualizar el css
# Aritza, 13/12/2014
# -*- coding: utf-8 -*-

import praw
import time
import unicodedata
import os
import urllib


# Contrasenas
adminUser = 'PlazaPodemos'
adminPass = ''


# Definiciones para el arichivo 
fLista = 'municipiosParcial.txt'
lista = []
subOrig = 'ClaroQuePodemos'
imgDir ='images/'



# Algunos contadores
numOk = 0
numError=0

# Cargamos los datos
os.system('clear')
print('Podemos!')

r = praw.Reddit(user_agent='FlairBotPodemos')
r.login( adminUser, adminPass )
r.config.decode_html_entities = True

with open(fLista) as f:
	lista = f.read().splitlines()

#Recogemos imagenes, estilos y la barra lateral del origen
images = r.get_stylesheet(subOrig)['images']
estilo = r.get_stylesheet(subOrig)['stylesheet']
barraLateral = r.get_settings(subOrig)
nuevoLateral = barraLateral['description']

# Descargamos los archivos que no esten cacheados para cachearlos
for img in images:
	filepath = imgDir + img['name']+'.png'
	if not os.path.isfile(filepath):
		urllib.urlretrieve(img['url'], filepath)

# Bucle principal 
for w in lista:
		#os.system('clear')
		subreddit = 'PlazaPodemos'+w

		print 'Actualizando: ', subreddit
		
		print ('Creo '+ subreddit + ' ?(s/n)')
		respuesta = raw_input()

		if respuesta == "s" : 
			
			print 'Creando: '+ subreddit
			#r.create_subreddit( nombreCorto, nombreLargo, language='es',subreddit_type='private', content_options='any', over_18=False, show_media=True )
			
			# Subir las imagenes
			print 'Subiendo las imagenes para: ',subreddit
			for img in images:
				filepath = imgDir + img['name'] + '.png'
				print 'Subiendo imagen: ',filepath 
				#r.upload_image(subreddit,filepath,name=img['name'],header=False)
			
			print 'Actualizando css'
			#r.set_stylesheet(subreddit, estilo)
			print 'Actualizando Barra Lateral'
			r.update_settings (r.get_subreddit(subreddit), description=nuevoLateral)


			numOk = numOk + 1
		else:
			numError = numError + 1

# Presenta algunos resultados:
print "Asignaciones con exito:", numOk
print "Asignaciones erroneas:", numError				
