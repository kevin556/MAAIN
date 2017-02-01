#!/usr/bin/python2.7

class Vecteur(object):

    vecteur=[]

    def __getitem__(self,index):
        return self.vecteur[int(index)]

    def __init__(self,*arg):
        if len(arg) == 1:
            for i in range(0,int(arg),1):
                self.vecteur.append(i)
        else:
            for i in range(0,len(arg),1):
                self.vecteur.append(i)
        