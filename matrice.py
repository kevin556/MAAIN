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
		table_c=[];table_l=[];table_i=[]
		matrice_size = matrice_a.shape[0]
		element_courant = 0
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
	nombre_sommet=0;nb_ligne = 0
	table_c =[];table_l =[0];table_i =[]
	element_courant = 0;element_courant_i = 0
	tmp_chiffre = 0
	f=open(fileName,'r')
	lignes = f.readlines()
	f.close()
	for ligne in lignes:
		'''
			pour eviter de prendre en compte les lignes en debut de fichier qui ne sont pas des chiffres
		'''
		if not (unicode(ligne.split("\t")[0]).isnumeric()):
			continue
		else:
			tmp = ligne.split("\t")
			if(tmp_chiffre == 0):
				tmp_chiffre = tmp[0]
			if(tmp[0] != tmp_chiffre):
				table_l.append(element_courant_i)
				nb_ligne+=1
				if(nombre_sommet == 0):
					nombre_sommet = element_courant_i
				element_courant=0

			print("gauche %s droite %s")%(tmp[0],tmp[1])
			table_c.append(tmp[0])
			element_courant+=1
			element_courant_i+=1
			table_i.append(element_courant)
			tmp_chiffre = tmp[0]


	print ("sommet %d ligne %d") %(nombre_sommet,nb_ligne)
	return table_c,table_l,table_i,nombre_sommet

