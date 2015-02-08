#!/usr/bin/python
# PlazaPodemos, copia asignaciones de etiquetas a plazas 
# Hay que editar los valores iniciales para que los use en la asignacion
# Aritza.

import praw
import time

# Contrasenas

adminUser = 'aritza'
adminPass = ''

# Valores iniciales 

plazaOrigen = 'podemos'
plazaDestino = ''


# Definiciones para el archivo

distintivo ='cc'

# Algunos contadores y valores

numError = 0
numOk = 0

# Cargamos los datos

print('Podemos!')
print 'recogiendo distintivos de ', plazaOrigen

r = praw.Reddit(user_agent='FlairBotPodemos')
r.login(adminUser, adminPass)

listaDistintivos = r.get_subreddit(plazaOrigen).get_flair_list(limit=None)

flairMap = []

for i in listaDistintivos:
	if i['flair_css_class'] == distintivo:
		flairMap.append(i)
		numOk = numOk + 1


#r.get_subreddit(plazaDestino).set_flair_csv(flairMap)

print "Asignaciones con exito:", numOk
print "Asignaciones erroneas:", numError				

