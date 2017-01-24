#!/usr/bin/python2.7
import numpy as np
from sys import argv

from matrice import Matrice
from vecteur import Vecteur



a = np.array([[0,0,1,0],[2,3,0,4],[0,5,6,7],[0,0,0,0]])
'''
b = np.array([[0,3,5,8],[1,0,2,0],[0,0,0,0],[0,3,0,0]])
d = np.array([[0,0,0,1/3],[1/2,0,0,1/3],[0,1,0,1/3],[1/2,0,1,0]])


c = Vecteur([2,3,1,3])
e = Vecteur([1,0,0,0])

tmp = Matrice(a)
tmp2 = Matrice(b)
print(c.calcul_matrice_by_vector(tmp))
print(c.calcul_matrice_by_vector(tmp2))
print(c.produit_transpose(tmp))
print(c.produit_transpose(tmp2))
print(e.produit_transpose(Matrice(d)))

print(tmp.tableau_c)
print(tmp.tableau_l)
print(tmp.tableau_i)
print(tmp2.tableau_c)
print(tmp2.tableau_l)
print(tmp2.tableau_i)
'''
#multiplie_matrice(a,a)
'''print(init_res_empty_matrix(a,a))'''

if(len(argv)==2):
	print argv[1]
	c = Matrice(argv[1])
else:
	d = Matrice(a)