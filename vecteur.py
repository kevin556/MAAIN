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
        return self.vecteur[int(index)]

    def __str__(self):
        s=""
        for i in range(0,len(self.vecteur)):
            s+="valeur de i %d -> %d\n"%(i,self.vecteur[i])
        return s

    def __init__(self,*arg):
        self.vecteur=[] 
        if len(arg) == 1:
            print('taille %d'%(int(arg[0])))
            self.vecteur.append(1)
            for i in range(1,int(arg[0]),1):
                self.vecteur.append(0)
        else:
            for i in range(0,len(arg),1):   
                self.vecteur.append(arg[i])
        