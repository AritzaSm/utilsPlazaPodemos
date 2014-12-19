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
fLista = 'comunidades.txt'
lista = []
subOrig = 'ClaroQuePodemos'
imgDir ='images/'



# Algunos contadores
numOk = 0
numError=0

# Cargamos los datos
os.system('clear')
print('Podemos!')

r = praw.Reddit(user_agent='PlazaPodemosBot')
#r = praw.Reddit('OAuth testing example by u/_Daimon_ ver 0.1 see ''https://praw.readthedocs.org/en/latest/' 'pages/oauth.html for source')

r.login( adminUser, adminPass )
r.config.decode_html_entities = True

with open(fLista) as f:
	lista = f.read().splitlines()

#Recogemos imagenes, estilos y la barra lateral del origen

	estilo = r.get_stylesheet(subOrig)['stylesheet']
	barraLateral = r.get_settings(subOrig)
	nuevoLateral = barraLateral['description']
	images = r.get_stylesheet(subOrig)['images']

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

# Recojo algunas variables, 

print 'Quieres crear plazas? (s/n)'
if raw_input() == 's':
	crearPlazas = True
else:
	crearPlazas = False

print 'Quieres actualizar las imagnes de las plazas? (s/n)'
if raw_input() == 's':
	actulizarImagenes = True
	CargaImagenes()
else:
	actulizarImagenes = False

print 'Quieres actualizar el CSS de plazas? (s/n)'
if raw_input() == 's':
	actualizarCss = True
else:
	actualizarCss = False

print 'Quieres replicar la barraLateral? (s/n)'
if raw_input() == 's':
	actualizarBarra = True
else:
	actualizarBarra = False

os.system('clear')

# Bucle principal 
for w in lista:
	os.system('clear')
	subreddit = w
	nombreLargo = w

	try:
	
			print 'Actualizando: ', subreddit
				
			if crearPlazas : 
				print 'Creando: '+ subreddit
				r.create_subreddit( subreddit , nombreLargo, language='es',subreddit_type='public', content_options='any', over_18=False, show_media=True )
						
			if actulizarImagenes : 
				print 'Subiendo las imagenes para: ',subreddit
				for img in images:
					filepath = imgDir + img['name'] + '.png'
					print 'Subiendo imagen: ',filepath
					r.upload_image(subreddit,filepath,name=img['name'],header=False)
					
			if actualizarCss : 
				print 'Actualizando css'
				r.set_stylesheet(subreddit, estilo)
					
			if actualizarBarra : 
				print 'Actualizando y personalizando la Barra Lateral'
				nuevoLateral = nuevoLateral.replace('/r/ClaroQuePodemos','/r/'+ subreddit )
				nuevoLateral = nuevoLateral.replace( '/r/'+subreddit+'/search?q=flair%3A%27Lemas31E%27','/r/podemos/search?q=flair%3A%27Lemas31E%27')
				r.update_settings (r.get_subreddit(subreddit), description=nuevoLateral)
					
			numOk = numOk +1		
	except praw.errors.RateLimitExceeded as error:
		print ('Esperando: %d seconds' %error.sleep_time)
		time.sleep(error.sleep_time)
		pass
	except praw.errors.ModeratorOrScopeRequired:
		numError = numError + 1
		pass
	    
	    

# Presenta algunos resultados:
print "Asignaciones con exito:", numOk
print "Asignaciones erroneas:", numError

# Borro la cache de archivos
BorraCache()

