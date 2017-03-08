#!/usr/bin/python2.7
from random import randint

#structure mot-page

d = {'mot1': {'idpage1': 1, 'idpage99': 2,'idpage100': 2}, 'mot2': {'idpage1': 3, 'idpage2': 4}}

#l'access  aux elements se fait comme suit ...


#l'ajout d'element one by one

def granola_de_prince(ded):
    myfile = open("graph_granola.txt", "w+")
    for key,value in ded.iteritems():
        myfile.write(key+'\n')
        for elem in value:
            try:
                myfile.write('\t'+elem+" "+str(ded[key][elem])+'\n')
            except KeyError:
                pass



granola_de_prince(d)