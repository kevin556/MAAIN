#!/usr/bin/python2.7
import numpy as np

class Matrice(object):
	
	def __init__(self,text):
		self.tableau_c = []
		self.tableau_l = []
		self.tableau_i = []
		self.nb_sommet = 0
		print(type(text))
		#we have to get the type of matrix
		if(isinstance(text,basestring)):
			self.tableau_c,self.get_from_filename(text)
		else:
			get_matrix_from_file(text)


	def get_from_filename(self,fileName):
		self.tableau_c,self.tableau_l, self.tableau_i,self.nb_sommet = get_matrix_from_file(fileName)

	def get_from_matrice(self,matrice_a):
		self.tableau_c,self.tableau_l, self.tableau_i = get_all_table(matrice_a)
		self.nb_sommet = matrice_a.shape[0]

	def produit_vecteur_matrix(self,vecteur_a):
		res=[]
		somme = 0
		for i in range(0,int(self.nb_sommet),1):
			for k in range(self.tableau_l[i],self.tableau_l[i+1],1):
				somme += self.tableau_c[k] * vecteur_a[self.tableau_i[k]]
			res.append(somme)
		return res

	def produit_transpose(self,vecteur_a):
		res=[]
		for i in range(0,self.nb_sommet,1):
			res.append(0)
		for i in range(0,self.nb_sommet,1):
			for j in range(self.tableau_l[i],self.tableau_l[i+1],1):
				res[self.tableau_i[j]] += self.tableau_c[j] * vecteur_a[i]
		return res


def get_matrix_from_file(fileName):
	nombre_sommet=0;nb_ligne = 0
	table_c =[];table_l =[0];table_i =[]
	f=open(fileName,'r')
	lignes = f.readlines()
	f.close()
	chiffre_lu=[];chiffre_gauche=0;chiffre_droit=0;chiffre_stocke=-1
	compteur_chiffre_gauche = 0
	for i in range(0,len(lignes),1):
		'''
			pour eviter de prendre en compte les lignes en debut de fichier qui ne sont pas des chiffres
		'''
		if not (unicode(lignes[i].split("\t")[0]).isnumeric()):
			continue
		else:
			chiffre_lu =lignes[i].strip("\n").strip('\r').split('	')
			chiffre_gauche = chiffre_lu[0]
			chiffre_droit = chiffre_lu[1]
			#pour l\'initialisation
			if chiffre_stocke == -1:
				chiffre_stocke = chiffre_gauche

			if chiffre_gauche != chiffre_stocke:
				#print 'compteur_chiffre_gauche %d chiffre_gauche %s chiffre_stocke %s' %(compteur_chiffre_gauche,chiffre_gauche,chiffre_stocke)
				for j in range(0,compteur_chiffre_gauche ,1):
					table_c.append(1/(float)(compteur_chiffre_gauche))
				table_l.append(table_l[-1]+compteur_chiffre_gauche)
				compteur_chiffre_gauche = 0
				chiffre_stocke = chiffre_gauche
			compteur_chiffre_gauche+=1
			table_i.append(chiffre_droit)
	print 'chiffre_stocke %s '%(chiffre_stocke)
	for i in range(0,compteur_chiffre_gauche,1):
		table_c.append(1/(float)(compteur_chiffre_gauche))
	table_l.append(len(table_c))
	print 'nb_lignes %d'%(len(lignes))
	print table_c
	print table_l
	print table_i
	nombre_sommet = chiffre_stocke
	return table_c,table_l,table_i,nombre_sommet


	


