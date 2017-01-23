#!/usr/bin/python2.7

import numpy as np

class Vecteur(object):

    def __init__(self,vecteur_c):
        self.vecteur = vecteur_c

    def calcul_matrice_by_vector(self,matrice_a):
        res=[]
        for i in range(0,matrice_a.nb_sommet):
            tmp=0.0
            for j in range(matrice_a.tableau_l[i],matrice_a.tableau_l[i+1]):
                tmp+= matrice_a.tableau_c[j] * self.vecteur[matrice_a.tableau_i[j]]
            res.append(tmp)
        return res

    def produit_transpose(self,matrice_a):
        
        res = matrice_a.dot(self.vecteur)
        return res