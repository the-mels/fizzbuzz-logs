import sys,csv
from collections import Counter
from itertools import groupby


with open(sys.argv[1], 'r') as input_dataset: # pour passer le fichier comme argument à partir du terminal
	viewmode_list = list() #On initialise une liste pour le comptage des mots successifs 
	viewmode_list2 = list() #On initialise une liste pour la récupération des zooms
	checklist = list()
	for line in input_dataset: #Pour chaque ligne dans le fichier d'entrée
	    listed_data = line.split(' ') #Split la ligne en 2 avec le délimiteur tab
	    viewmode = listed_data[1].split('/') #Split le second argument de la liste contenant la tuile de plan selon le délimiteur slash
	    if (len(viewmode)==9): #Il faut que la liste splitté via slash contiennent 9 éléments comme décrit dans la structure de base (ex:/map/1.0/slab/standard_hd/256/14/8620/6047)
	        viewmode_list.append(viewmode[4]) #La liste va recevoir à chaque ligne un viewmode qui s'ajoute en fin de liste
	        viewmode_list2.append((viewmode[4],viewmode[6])) #La liste va recevoir à chaque ligne un viewmode qui s'ajoute en fin de liste     
	groups = groupby(viewmode_list)  
	result = [(label, sum(1 for _ in group)) for label, group in groups]#Compte les occurences identiques successives de chaque viewmode
	j=0
	x=0
	while j < len(viewmode_list2) : #parcourir la liste contenant les viewmodes associés aux zooms
	    while x < len(result) and j < len(viewmode_list2) and viewmode_list2[j][0] == result[x][0]   :  #  
	        if (viewmode_list2[j][1] not in checklist): #Verifier que le zoom lu n'est pas présent dans la checklist pour éviter les doublons
	            checklist.append(viewmode_list2[j][1]) #Dans ce cas ajouter la valeur du zoom dans la liste du viewmode
	        j=j+1
	    print(result[x][0],"\t",result[x][1],"\t",", ".join(checklist)) # aficher le résultat dans le format demandé
	    checklist.clear() #vider la liste des zooms de l'ancien viewmode
	    x=x+1
