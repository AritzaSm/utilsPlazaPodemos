 #!/usr/bin/python
 # PlazaPodemos, asignacion de etiquetas a usuarios a lo bruto ;)
 # soportevotaciones@podemos.info

import praw
import time

# Contrasenas

adminUser = ''
adminPass = ''


# Definiciones para los archivos

fListaSG = 'fListaSg.txt'
listaSG = []
fListaCC = 'fListaCC.txt'
listaCC = []
fListaCG = 'fListaCG.txt'
listaCG = []

# Algunos contadores

numError=0
numCG=0
numCC=0

# Cargamos los datos

print('Podemos!')

r = praw.Reddit(user_agent='FlairBotPodemos')
r.login(adminUser, adminPass)

with open(fListaSG) as f:
	listaSG = f.read().splitlines()

with open(fListaCC) as f:
	listaCC = f.read().splitlines()

with open(fListaCG) as f:
	listaCG = f.read().splitlines()


print('Anadiendo etiquetas a las/as candidatas/os...')


#Pone las etiquetas de la "Comision de garantias"
for w in listaCG:
	try:
		r.get_subreddit('podemos').set_flair(w,'Comision garantias','cg')
	
	except praw.errors.InvalidFlairTarget:
		print 'Error: El usuario: ',w,' no existe'
		numError=numError+1
	else:
		numCG=numCG+1
#Pone las etiquetas del "Consejo ciudadano"
for w in listaCC:
	try:
		r.get_subreddit('podemos').set_flair(w,'Consejo ciudadano','cc')
	except praw.errors.InvalidFlairTarget:
		print 'Error: El usuario ',w,' no existe'
		numError=numError+1
	else:
		numCC=numCC+1

print "Asignaciones con exito:"
print "Comision garantias:", numCG
print "Consejo ciudadano:", numCC
print "Asignaciones erroneas:", numError				


