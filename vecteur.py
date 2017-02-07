#!/usr/bin/python2.7
import math

class Vecteur(object):
   
    def somme_vecteur(self,vecteur_b):
        somme = 0.0
        #self.vecteur et vecteur_b ont la meme taille puisque ce sont deux iterations du meme vecteur
        if( len(self.vecteur) == len(vecteur_b.vecteur)):
            for i in range(0,len(vecteur_b.vecteur),1):
               
                if(self.vecteur[i]!=0 and vecteur_b[i] != 0):
                    print "valeur de i %d"%(i)
                somme += self.vecteur[i] + vecteur_b[i]
            somme = math.sqrt(somme)
            return somme

    def __getitem__(self,index):
        if(index < len(self.vecteur)):
            return self.vecteur[int(index)]


    def __str__(self):
        s=""
        for i in range(0,len(self.vecteur)):
            s+="valeur de i %d -> %d\n"%(i,self.vecteur[i])
        return s

	#self,sommet_depart,*arg
    def __init__(self,*arg):
    	print "taille de init %d\n"%(len(arg))
        self.vecteur = [0] * arg[0]
        if(len(arg) == 2):
        	self.vecteur[int(arg[1])] = 1
        else:
        	self.vecteur[0] = 1


    def pagerank_zero(self,vecteur_a,sommet_depart,epsilon):
		while self.somme_vecteur(vecteur_a)>epsilon:
			print "la"

