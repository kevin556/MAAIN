#!/usr/bin/python2.7


class Matrice(object):

	def __init__(self,text):
		self.tableau_c,self.tableau_l,self.tableau_i,self.nb_colonne = get_matrix_from_file(text)

	def produit_direct(self,vecteur_a):
		n = int(self.nb_colonne)
		res =[]
		for i in range(0,n,1):
			somme = 0.0
		#	print "difference %f %f \n"%(int(self.tableau_l[i]),int(self.tableau_l[i+1]))
			for k in range(int(self.tableau_l[i]), int(self.tableau_l[i+1]) , 1):
				print "%f * %f -> %f "%(float(self.tableau_c[k]),float(vecteur_a.vecteur[int(self.tableau_i[k])]),float(self.tableau_c[k]) * float(vecteur_a.vecteur[int(self.tableau_i[k])]))
				somme += float(self.tableau_c[k]) * float(vecteur_a.vecteur[int(self.tableau_i[k])])
		#		print "somme %f"%(somme)
			res.append(somme)
		return res


	def produit_transpose(self,vecteur_a):
		res=[]
		for i in range(0,self.nb_colonne ,1):
			res.append(0.0)
		for i in range(0,self.nb_colonne,1):
		#	print "valeur de i %d "%(i)
			for j in range(int(self.tableau_l[i]),int(self.tableau_l[i+1]),1):
		#		print "valeur de j %d "%(j)
		#		print "self.tableau_i[j]) %d self.tableau_c[j] %f vecteur_a.vecteur[i] %f \n"%(int(self.tableau_i[j]),float(self.tableau_c[j]),float(vecteur_a.vecteur[i]))
		#		print res[int(self.tableau_i[j])]
				res[int(self.tableau_i[j])] += float(self.tableau_c[j]) * float(vecteur_a.vecteur[i])
		return res

def get_matrix_from_file(fileName):
	chiffre_lu=[];chiffre_gauche=0;chiffre_droit=0;chiffre_stocke=-1
	compteur_chiffre_gauche = 0
	table_c=[];table_l=[0];table_i=[]
	f=open(fileName,'r')
	lignes = f.readlines()
	f.close()

	for i in range(0,len(lignes)):
		if "#" in lignes[i]:
			if "Nodes:" in lignes[i]:
				nb_colonne = int(lignes[i].split(" ")[2])
			continue
		chiffre_lu =lignes[i].strip("\n").strip('\r').split('	')
		chiffre_gauche = chiffre_lu[0]
		chiffre_droit = chiffre_lu[1]
		#pour l\'initialisation
		if chiffre_stocke == -1:
			chiffre_stocke = chiffre_gauche
		
		if chiffre_gauche != chiffre_stocke:
			tmp = int(chiffre_gauche) - (int(chiffre_stocke) +1 )
			if( tmp >= 0):
				for i in range(0,tmp,1):
					table_l.append(table_l[-1])
			for j in range(0,compteur_chiffre_gauche ,1):
				table_c.append(1/(float)(compteur_chiffre_gauche))
			table_l.append(table_l[-1]+compteur_chiffre_gauche)
			compteur_chiffre_gauche = 0
			chiffre_stocke = chiffre_gauche
		compteur_chiffre_gauche+=1
		table_i.append(chiffre_droit)

	for i in range(0,compteur_chiffre_gauche,1):
		table_c.append(1/(float)(compteur_chiffre_gauche))
	if(int(chiffre_stocke) < nb_colonne -1):
		print "rami\n"
		for i in range(int(chiffre_stocke),nb_colonne,1):
			table_l.append(table_l[-1])
	
	table_l.append(len(table_c))
	
	return table_c,table_l,table_i,nb_colonne