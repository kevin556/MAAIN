#!/usr/bin/python2.7
from sys import argv
from matrice_new import Matrice
from vecteur import Vecteur


def pagerank_zap(matrice,epsilon,sommet_depart,d):
	compteur = 0
	n = matrice.nb_colonne
	v0 = Vecteur(matrice.nb_colonne,sommet_depart,"zap")
	v1 = Vecteur(matrice.nb_colonne,sommet_depart,"zap")
	v2 = Vecteur(matrice.nb_colonne,sommet_depart)
	zap = (((float(d)/float(n)) + (1 - float(d))))
	while(True):
		compteur+=1
		v1.vecteur = m.produit_transpose(v0)
		for i in range(0,m.nb_colonne,1):
			v1.vecteur[i]*= zap
		print "vecteur iteration %d : %s\n"%(compteur,v1.vecteur)
		v2.vecteur = v1.soustraction_vecteur(v0)
		
		if((v2.norme())>=epsilon):
			v0.vecteur = m.produit_transpose(v1)
			for i in range(0,m.nb_colonne,1):
				v0.vecteur[i]*= zap
		else:
			break
			
	print "vecteur zap final %s" %(v1.vecteur)


if len(argv) == 5:
	sommet_depart = int(argv[2])
	epsilon = float(argv[3])
	d=float(argv[4])
	if(d == 0.1 or d==0.2):
		res = []
		m = Matrice(argv[1])
		pagerank_zap(m,epsilon,sommet_depart,d)
	else:
		print "mauvais facteur zap"
else:
	print "usage ./programme fichier_source sommet_depart epsilon zap"


