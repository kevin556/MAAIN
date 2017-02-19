#!/usr/bin/python2.7
from sys import argv
from matrice_new import Matrice
from vecteur import Vecteur

if len(argv) == 4:
	sommet_depart = int(argv[2])
	nb_pas = int(argv[3])
	res = []
	m = Matrice(argv[1])
	v = Vecteur(m.nb_colonne,sommet_depart)
	print "sommet_depart %d nb_pas %d \n"%(sommet_depart,nb_pas)
	for i in range(0,nb_pas,1):
		print "matrice_tableau_c %s \n"%(m.tableau_c)
		print "v.vecteur avant assignation %s \n"%(v.vecteur)
		v.vecteur = m.produit_transpose(v)
		print "iteration %d %s \n"%(i+1,v.vecteur)

else:
	print "usage ./programme fichier_source sommet_depart nombre_de_pas"
