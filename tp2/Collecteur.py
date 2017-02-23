#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from sys import argv
from Dictionnaire import get_word_file
from itertools import izip
from unidecode import unidecode
import copy


class Collecteur:
    mots = []
    titre_id = {}   #Structure (titre , id)
    mot_page ={}   #Structure (mot , {idpage:apparition})
    mot_page_frequence ={}   #Structure (mot , {idpage:frequence})


    #quand est ce que c'est appele ?
    def process_buffer(buf):
        tnode = ET.fromstring(buf)
        #pull it apart and stick it in the database

    def make_file_and_word_list_from_file(filename):
        get_word_file(filename)
        import_dico(filename)

    def import_dico(self,filename_dico = 'dictionnaire.txt'):
        self.mots = [line.rstrip('\n') for line in open(filename_dico)]   

    '''def create_tmp_dico(self):
        tmp = [0] * len(self.mots)
        self.dico_tmp = dict(izip(self.mots, tmp))'''
    
    def do_the_harlem_shake(self,fileName):
        #Moncef pense que ça ne plantera pas
        id_get = False;tmp = False;tmp2 = False
        inputbuffer="";titre="";idp=""

        with open(str(fileName),'rb') as inputfile:
            append = False
            for line in inputfile: 
                if '<page>' in line or tmp:
                    tmp = True
                    #on entre dans la page
                    if '<title>' in line and '</title>' in line:
                        titre = line.replace('<title>',"").replace('</title>',"").strip()
                    if '<id>' in line and '</id>' in line and not id_get:
                        idp = line.replace('<id>',"").replace("</id>","").strip()
                        id_get = True
                    if '<text>' in line and '</text>' in line:
                        inputbuffer+= line.replace('<text>',"").replace('</text>',"").strip()
                    
                    elif '<text' in line or tmp2:
                        tmp2 = True
                        inputbuffer+= line.replace('<text>',"").replace("</text>","").strip()+" "
                    
                    if '</text>' in line and tmp2:
                        inputbuffer+= line.replace('<text>',"").replace("</text>","").strip()+" "
                        tmp2 = False

                if '</page>' in line:
                    print "titre %s \n"%(titre)
                    print "id %s \n"%(idp)
                    print "text %s \n"%(inputbuffer)
                    self.analyse_page(idp,inputbuffer+" "+titre)
                    id_get = False;tmp = False;tmp2 = False
                    inputbuffer="";titre="";idp=""
                


    def analyse_page(self,idp,text_to_analyse):
        print 'TEXT', text_to_analyse
        page_length = len(str.split(text_to_analyse," "))
        print 'TOTAL', page_length

        for mot in str.split(text_to_analyse," "):
            if mot in self.mots:
                #Si le mot existe dans la structure mot_page
                if mot in self.mot_page:
                    #Si l'ID de la page existe on incrémente SINON on rajoute l'id avec un compteur = 1
                    if idp in self.mot_page[mot]:
                        self.mot_page[mot][idp] += 1
                    else:
                        self.mot_page[mot][idp] = 1
                else:   
                    self.mot_page[mot] = {}
                    self.mot_page[mot][idp] = 1
        dic = copy.deepcopy(self.mot_page.copy())
        self.mot_page_frequence = self.rami_money(page_length,dic)    
                
    def rami_money(self, total, dic):
        for mot in dic:
            for idpage in dic[mot]:
                dic[mot][idpage] = (float)(dic[mot][idpage]) / total
        return dic







    def resultat(self):
        print 'RESULTAT', self.mot_page
        print 'FREQUENCE', self.mot_page_frequence

                        
#fonction a travailler car certains mots ne doivent pas être pris en compte
def format_mot(mot):
    return mot.replace(" ","").replace("'","").replace(",","").replace("l'","").strip()


if __name__ == '__main__':
    if(len(argv)==2):
        a = Collecteur()
        a.import_dico()
        #a.create_tmp_dico()
        a.do_the_harlem_shake(argv[1])
        a.resultat()
    else:
        print("mauvaise utilisation\nusage:./Collecteur.py option filename")