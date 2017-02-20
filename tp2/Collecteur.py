#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from sys import argv
from Dictionnaire import get_word_file
from itertools import izip
from unidecode import unidecode

class Collecteur:
    mots = []
    titre = {}
    dico = {}
    dico_tmp={}
    dico_frequence={}
    index_courant = 0
    #quand est ce que c'est appele ?
    def process_buffer(buf):
        tnode = ET.fromstring(buf)
        #pull it apart and stick it in the database

    def make_file_and_word_list_from_file(filename):
        get_word_file(filename)
        import_dico(filename)

    def import_dico(self,filename_dico = 'dictionnaire.txt'):
        self.mots = [line.rstrip('\n') for line in open(filename_dico)]   

    def create_tmp_dico(self):
        tmp = [0] * len(self.mots)
        self.dico_tmp = dict(izip(self.mots, tmp))
    
    def do_the_harlem_shake(self,fileName):
        #Moncef pense que ça ne plantera pas
        tmp =False;tmp2=False;tmp3 = True
        with open(str(fileName),'rb') as inputfile:
            inputbuffer=""
            titre=""
            id=""
            for line in inputfile:
                if '<page>' in line:
                    #on entre dans la page
                    tmp = True
                if tmp:
                    #on est dans la page
                    if '<title>' in line and '</title>' in line:
                        titre+=line.replace("<title>","").replace("</title>","").strip()
                    if '<id>' in line and '</id>' in line:
                        if tmp3:
                            id+=line.replace("<id>","").replace("</id>","").strip()
                        tmp3 = False
                        print("id %s \n")%(id)
                    if 'text' in line:
                        inputbuffer+=line.replace("<text>","").strip()
                        tmp2=True
                    if tmp2:
                        print line
                        inputbuffer+=line
                    if '</text>' in line:
                        inputbuffer+=line.replace("</text>","").strip()
                        tmp2 = False
                if '</page>' in line:
                    self.analyse_page(id,inputbuffer)
                    break
                    tmp3 = True
                    titre = ""
                    id=""
                    inputbuffer = ""
                    tmp = False



    def analyse_page(self,id,text_to_analyse):
        compteur_mot = 0
        compteur_text = 0
        for mot in str.split(text_to_analyse," "):
            if format_mot(mot) in self.dico:
                compteur_mot = compteur_mot+1
                #il faut trouver comment acceder a la liste
                self.dico[mot].value = self.dico[mot].value+1
                

        print compteur_mot
         
#fonction a travailler car certains mots ne doivent pas être pris en compte
def format_mot(mot):
    return mot.replace(" ","").replace("'","").replace(",","").strip()


if __name__ == '__main__':
    if(len(argv)==3):
        a = Collecteur()
        a.import_dico()
        a.create_tmp_dico()
        a.do_the_harlem_shake(argv[2])
    else:
        print("mauvaise utilisation\nusage:./Collecteur.py option filename")