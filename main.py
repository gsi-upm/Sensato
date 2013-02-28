# -*- coding: utf-8 -*-
# agente personal para el hogar con razonamiento basado en sentido

import sys
from accessAPI import accessAPI

def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices

def getOptions(actions,deep):
	actionsToPerform = list()
	for action in actions:
		try:
			actionsToPerform.index(action[deep])
		except ValueError:
			actionsToPerform.append(action[deep])
	print actionsToPerform
	nombre = raw_input('¿Qué opción quieres tomar? ')
	try:
		indexes = all_indices(nombre, actions)
		print indexes
	except ValueError:
		print 'Esa opción no está disponible'

if(len(sys.argv) > 1):

	mipeticion = accessAPI(str(sys.argv[1]),str(sys.argv[2]))
	mipeticion.getActions() 
	actions = mipeticion.results
	getOptions (actions, 0)

	

else:
	print "Debes indicar el elemento que quieres buscar" 
	
