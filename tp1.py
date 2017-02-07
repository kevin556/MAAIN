#!/usr/bin/python2.7
from sys import argv

from matrice_new import Matrice
from vecteur import Vecteur

c = Matrice(argv[1])
print c.tableau_l
print(c.tableau_c)

f = Vecteur(c.nb_colonne,0)
f.vecteur = [0.0,0.5,0.0,0.5]
print f.vecteur
print c.produit_direct(f)
print(c.produit_transpose(f))


'''
f = Vecteur(55,c.nb_colonne)
print(f)

a = c.produit_direct(f)
'''

#print(a.somme_vecteur(b))
#