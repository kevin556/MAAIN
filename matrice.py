#!/usr/bin/python2.7
import numpy as np

class Matrice(object):
	
	def __init__(self,text):
		self.tableau_c = []
		self.tableau_l = []
		self.tableau_i = []
		self.nb_sommet = 0
		if(isinstance(text,basestring)):
			self.tableau_c,self.get_from_filename(text)
		else:
			get_from_matrice(text)


	def get_from_filename(self,fileName):
		self.tableau_c,self.tableau_l, self.tableau_i,self.nb_sommet = get_matrix_from_file(fileName)

	def get_from_matrice(self,matrice_a):
		self.tableau_c,self.tableau_l, self.tableau_i = get_all_table(matrice_a)
		self.nb_sommet = matrice_a.shape[0]

def get_all_table(matrice_a):
	#on part du principe que la matrice est de taille n * n
	table_c=[]
	table_l=[]
	table_i=[]
	matrice_size = matrice_a.shape[0]
	element_courant = 0
	element_courant_tmp=0
	for i in range(matrice_size):
		table_l.append(element_courant)
		for j in range(matrice_size):
			if(matrice_a[i][j] !=0.0):
				table_c.append(matrice_a[i][j])
				element_courant+=1		
				table_i.append(j)
	table_l.append(len(table_c))
	return table_c,table_l,table_i

def get_matrix_from_file(fileName):
	f=open(fileName,'r')
	print(type(f))
	lignes = f.readlines()
	f.close()
	for ligne in lignes:
		print ligne
	
