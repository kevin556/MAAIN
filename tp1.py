#!/usr/bin/python2.7
from sys import argv

from matrice_new import Matrice
from vecteur import Vecteur

c = Matrice(argv[1])
print c.tableau_c;
print c.tableau_l;
print c.tableau_i;
print(c.nb_colonne)

f = Vecteur(0,c.nb_colonne)
print(f)

a = c.produit_direct(f)
print ("produit direct %s " %(a))

'''
print(a.somme_vecteur(b))
'''

print(c.produit_transpose(f))
