#!/usr/bin/python
# PlazaPodemos: Script para la creacion de plazas ;)
# Datos necesarios: 'NombreCorto', 'nombre largo', 'una descripcion del sitio' 
#

import praw
import time

# Contrasenas

adminUser = ''
adminPass = ''


# Definiciones para los archivos

fListaPlazas = 'fListaPlazas.txt'
listaPlazas = []

# Algunos contadores

numError=0
numPlazas=0

# Cargamos los datos

print( 'Podemos!' )
print( 'Cargando datos...' )

# Inicializo los objetos para la api

r = praw.Reddit(user_agent='FlairBotPodemos')
r.login(adminUser, adminPass)

with open(fListaPlazas) as f:
	listaPlazas = f.read().splitlines()

print( 'Creando plazas...' )


# Crea nuevas Plazas

for w in listaCG:
	try:
		# r.get_subreddit('podemos').set_flair(w,'Comision garantias','cg')
	
	except praw.errors.InvalidFlairTarget:
		print 'Error: El usuario: ',w,' no existe'
		numError=numError+1
	else:
		numCG=numPlazas+1

# Resultados finales 

print( 'Creaciones con exito' )
print( 'Han ido bien', numPlazas )
print( 'Erroneas: ', numError ) 

