 #!/usr/bin/python
 # PlazaPodemos, asignacion de etiquetas a usuarios a lo bruto ;)
 # Hay que editar los valores iniciales para que los use en la asignacion
 # Aritza.

import praw
import time

# Contrasenas

adminUser = ''
adminPass = ''

# Valores iniciales 

plaza = ''
textoPegatina = ''
clasePegatina = ''


# Definiciones para el archivo

fLista = 'fLista.txt'
lista = []

# Algunos contadores y valores

numError = 0
numOk = 0

# Cargamos los datos

print('Podemos!')
print 'Asignando etiquetas para ', plaza

r = praw.Reddit(user_agent='FlairBotPodemos')
r.login(adminUser, adminPass)

with open(fLista) as f:
	lista = f.read().splitlines()


print('Anadiendo etiquetas a las/as candidatas/os...')


#Pone las etiquetas de q los usuarios 

for w in lista:
	try:
		r.get_subreddit(plaza).set_flair(w,textoPegatina,clasePegatina)
	
	except praw.errors.InvalidFlairTarget:
		print 'Error: El usuario: ',w,' no existe'
		numError=numError+1
	else:
		numOk=numOk+1

print "Asignaciones con exito:", numOk
print "Asignaciones erroneas:", numError				


