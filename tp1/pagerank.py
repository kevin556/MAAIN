#!/usr/bin/python2.7
import math
from matrice import Matrice
class pagerank(object):

	def __init__(self,matrice_a,vecteur_b):
	self.pagerank=[]
	self.matrice = matrice_a
	self.vecteur = vecteur_b
	self.vecteur = vacteur_c
	self.epsilon=0.015
	self.delta=0.0
	self.d=1.5



	calcul_pagerank(x):
		x=calcul_vectorz(matrice_a)
		while self.epsilon> delta:

			x=Matrice.produit_tranpose(matrice_a,x)
			delta= calcul_norm(x,y)

	return x


			



	calcul_norm(y,z):

		return math.hypot(y,z)


		