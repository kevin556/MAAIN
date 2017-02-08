#!/usr/bin/python2.7
from sys import argv
from matrice_new import Matrice
from vecteur import Vecteur


def pagerank_zap(matrice,epsilon,sommet_depart,d):
	compteur = 0
	n = matrice.nb_colonne
	v0 = Vecteur(matrice.nb_colonne,sommet_depart)
	v1 = Vecteur(matrice.nb_colonne,sommet_depart)
	v2 = Vecteur(matrice.nb_colonne,sommet_depart)
	while(True):
		compteur+=1
		v1.vecteur = m.produit_transpose(v0)
		print "vecteur %d : %s\n"%(compteur,v1.vecteur)
		v2.vecteur = v1.soustraction_vecteur(v0)
		if((v2.norme())>=epsilon):
			v0.vecteur = m.produit_transpose(v1)
		else:
			break
			
	for i in range (0,len(v1.vecteur)):
		v1.vecteur[i]=(d/n+(1-d)*v1.vecteur[i])

	print "vecteur zap %s" %(v1.vecteur)



if len(argv) == 5:
	sommet_depart = int(argv[2])
	epsilon = float(argv[3])
	d=float(argv[4])
	res = []
	m = Matrice(argv[1])
	pagerank_zap(m,epsilon,sommet_depart,d)
else:
	print "usage ./programme fichier_source sommet_depart epsilon zap"


