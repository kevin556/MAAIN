#!/usr/bin/python2.7
from Requete import *

if __name__ == '__main__':
	if len(argv) == 1:
		print("erreur aucun arguement pour la recherche")
	elif len(argv)> 10 : 
		print("erreur trop de mot pour la recherche")
	else:
		fichier_sortie_nom = enleve_doublon(argv)
		fichier_sortie = open("-".join(fichier_sortie_nom),"w+")
		fichier_sortie.write(algo_recherche(fichier_sortie_nom,"/Users/kevin/Desktop/graph_maain/graph_granola.txt"))
