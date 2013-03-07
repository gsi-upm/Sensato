# -*- coding: utf-8 -*-
# agente personal para el hogar con razonamiento basado en sentido

import sys
from accessAPI import accessAPI

def all_indices(value, qlist): #temp, not used
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
			actionsToPerform.index(action[deep])#if it is added, we do not add it twice
		except ValueError:
			actionsToPerform.append(action[deep])#if it is not added to the list, we append it.
		except IndexError:
			print 'The END' #FINISH!
	print actionsToPerform
	nombre = raw_input('¿Qué opción quieres tomar? ')
	filteredActions = [action for action in actions if action[deep]==nombre] #only the branches conducting to a solution
	getOptions(filteredActions, deep+1) #navigate recursively through the branch

if(len(sys.argv) > 2):

	mipeticion = accessAPI(str(sys.argv[1]),str(sys.argv[2]))
	mipeticion.getActions() 
	actions = mipeticion.results
	getOptions (actions, 0)

	

else:
	print "\nYou should indicate the host and the term to search\n\nFor example python main.py http://127.0.0.1:8084 vernoticias\n" 
	
