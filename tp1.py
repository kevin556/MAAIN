#!/usr/bin/python2.7
import numpy as np
from sys import argv

from matrice import Matrice
from vecteur import Vecteur



a = np.array([[0,0,1,0],[2,3,0,4],[0,5,6,7],[0,0,0,0]])
c = Matrice(argv[1])
d = Vecteur(0,0,0,1)
print(c.produit_vecteur_matrix(d))

