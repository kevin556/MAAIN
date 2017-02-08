#!/usr/bin/python2.7
from math import *

class Vecteur(object):
   
    def norme(self):
        somme = 0.0
        for i in range(0,len(self.vecteur),1):
        	somme += pow(self.vecteur[i],2)    
#        	print "somme %f \n"%(somme)
        return sqrt(somme)

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
        nb_element = int(arg[0])
    	#print "taille de init %d\n"%(len(arg))
        self.vecteur = [0] * nb_element
        if(len(arg) == 2):
        	self.vecteur[int(arg[1])] = 1
        if(len(arg) == 3):
            for i in range(0,nb_element,1):
                self.vecteur[i] = 1/float(nb_element)
        else:
        	self.vecteur[0] = 1


    def soustraction_vecteur(self,vecteur_b):
    	res=[]
    	for i in range(0,len(vecteur_b.vecteur),1):
    		res.append(float(self.vecteur[i]) - float(vecteur_b.vecteur[i]))
    	return res
