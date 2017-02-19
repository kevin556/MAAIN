#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from sys import argv
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode


delete_list = ["et","le", "la", "les",
			"un", "une", "a", "en", "sa", "son", "ses", "ma", "mon", "mes",
			"ta", "ton", "tes", "de", "du", "des", "au", "aux", "etc", "ce",
			"cet", "cette", "ceux", "celui", "celle", "ca", "ça", "pas", "rien",
			"aucun", ""]

#addresse ="32 rue d'Athènes Paris France Île-de-france Éve"
#print unidecode(addresse.decode('utf-8'))
def get_word_file(delete_list,filename):
    urls =[];soups =[];mots = [];tmp_liste=[]

    for i in range(1,11):
        urls.append('https://fr.wiktionary.org/wiki/Wiktionnaire:10000-wp-fr-'+str(i)+'000')

    for url in urls :
        pg = requests.get(url,verify=False)
        soups.append(BeautifulSoup(pg.content, "lxml"))

    for soup in soups:
        mots.append(soup.find_all("div",{"id":"mw-content-text"}))
    
    myfile = open(filename, "w+")
    
    for item in mots:
        for i in item:
            for j in i.find_all('ul'):
                for k in j.find_all('li'):
                    for m in k.find_all('a'):
                    	tmp = unidecode(m.text.encode('utf-8').strip().decode('utf-8')).lower()
                    	if tmp not in delete_list and tmp not in tmp_liste and tmp.isalpha() : #and len(tmp)> 1 -> constante mathematique ?
                    		tmp_liste.append(tmp)
    tmp_liste.sort()
    for item in tmp_liste:
	   myfile.write(item+'\n')


if __name__ == '__main__':
    if(len(argv)==2):
        get_word_file(delete_list,argv[1])
    else:
        print 'mauvaise utilisation\nusage ./Dictionnaire.py filename'