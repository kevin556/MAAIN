#!/usr/bin/python2.7
from sys import argv
from matrice_new import Matrice
from vecteur import Vecteur


def pagerank_zero(matrice,epsilon):
	compteur = 0
	v0 = Vecteur(matrice.nb_colonne,"zap","tmp")
	v1 = Vecteur(matrice.nb_colonne,"zap","tmp")
	v2 = Vecteur(matrice.nb_colonne)
	while(True):
		compteur+=1
		v1.vecteur = m.produit_transpose(v0)
		print "vecteur %d : %s\n"%(compteur,v1.vecteur)
		v2.vecteur = v1.soustraction_vecteur(v0)
		if((v2.norme())>=epsilon):
			v0.vecteur = m.produit_transpose(v1)
		else:
			break
	
if len(argv) == 3:
	res = []
	m = Matrice(argv[1])
	epsilon = float(argv[2])
	pagerank_zero(m,epsilon)
else:
	print "usage ./programme fichier_source  epsilon"
