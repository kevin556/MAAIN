#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from sys import argv
from Dictionnaire import get_word_file
from itertools import izip
from unidecode import unidecode
import copy
import re


class Collecteur:
    mots_liste = []
    mots ={}
    titre_id = {}   #Structure (titre , id)
    mot_page ={}   #Structure (mot : {idpage:apparition})
    mot_page_frequence ={}   #Structure (mot : {idpage:frequence})
    graph_nutella ={} #structure {idpage : [liens en titre]} les titres on va les traduire en IDs via la structure titre_id



    def make_file_and_word_list_from_file(filename):
        get_word_file(filename)
        import_dico(filename)

    def import_dico(self,filename_dico = 'dictionnaire.txt'):
        self.mots_liste = [line.rstrip('\n') for line in open(filename_dico)]
        for mot in self.mots_liste:
            self.mots[mot] = 1


    def trump(self,text):
        text=  unidecode(text.decode('utf-8')).encode('utf-8').lower()
        return text

    def do_the_harlem_shake(self,fileName):
        titre="";idp="";inputbuffer="";
        tag="{http://www.mediawiki.org/xml/export-0.10/}"
        context = ET.iterparse(fileName, events=("start", "end"))
        context = iter(context)
        event, root = context.next()
        for event, elem in context:
            if event == "end" and elem.tag == tag+"page":
                titre = elem.findtext(tag+"title").encode('utf-8')
                idp = elem.findtext(tag+"id")
                self.titre_id[titre] = idp
                a = elem.find(tag+"revision")
                inputbuffer = a.findtext(tag+"text").encode('utf-8')
                elem.clear()                
                print '<'+idp+'>', titre
                self.analyse_page(idp,inputbuffer+" "+titre)
                self.graph_nutella[idp] = self.get_all_links(inputbuffer)
                titre="";idp="";inputbuffer="";


    def get_all_links(self,text):
        links=[]
        tmp = str.split(text,'\n')
        for elem in tmp:
            links= links + (re.findall("\[\[(.*?)\]\]", elem))
        
        for link in links:
            if ':' in link:
                links.remove(link)
            elif '|' in link:
                links.remove(link)
                links.append(link.split('|')[0])
        return links

    def update_graph(self):
        for key, value in self.graph_nutella.iteritems():
            for n,i in enumerate(value):
                if self.trump(i) in self.titre_id:
                    value[n]= self.titre_id[i]

    def tartiner_nutella(self):
        myfile = open("graph_nutella.txt", "w+")
        for key,value in self.graph_nutella.iteritems():
            for n,i in enumerate(value):
                myfile.write(key+" "+value[n]+'\n')
                        
    def analyse_page(self,idp,text_to_analyse):
        #print 'TEXT', text_to_analyse
        #tmp = str.split(text_to_analyse," ")
        #page_length = len(tmp)
        #print 'TOTAL', page_length
        tmp2 = str.split(text_to_analyse,"\n")
        for item in tmp2:
            tmp3 = str.split(item," ")
            for i in tmp3:
                if " " in i or not i.isalpha():
                    tmp3.remove(i)
                else:
                    i = self.trump(i)
            for mot in tmp3:
                #Si le mot existe dans notre dictionnaire de mots
                try:
                    if self.mots[mot.lower()] == 1:                    
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
                except KeyError:
                    continue

                tmp3.remove(mot)

        #dic = self.mot_page
        #self.mot_page_frequence = self.rami_money(page_length,dic)    
                
    def rami_money(self, total, dic):
        for mot in dic:
            for idpage in dic[mot]:
                dic[mot][idpage] = (float)(dic[mot][idpage]) / total
        return dic


    def resultat(self):
        print 'MOT-PAGE', self.mot_page
        print '________________________________________________________________________________'
        print 'FREQUENCE', self.mot_page_frequence        
        print '________________________________________________________________________________'
        print 'TITRE-ID', self.titre_id
        print '________________________________________________________________________________'
        print 'GRAPH_nutella', self.graph_nutella
        
    def resultat2(self):
        print '________________________________________________________________________________'
        print 'GRAPH_nutella_UPDATED', self.graph_nutella


                        
#fonction a travailler car certains mots ne doivent pas être pris en compte ----> RAMI WHERE THE HELL ARE YOU ?
def format_mot(mot):
    return mot.replace(" ","").replace("'","").replace(",","").replace("l'","").strip()


if __name__ == '__main__':
    if len(argv)==2 :
        a = Collecteur()
        a.import_dico()
        a.do_the_harlem_shake(argv[1])
        a.resultat()
        a.update_graph()
        a.resultat2()
        a.tartiner_nutella()

    else:
        print("mauvaise utilisation\nusage:./Collecteur.py option filename")