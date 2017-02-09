#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

urls =[]
soups =[]
mots = []

delete_list = ["et","le", "la", "les",
			"un", "une", "a", "en", "sa", "son", "ses", "ma", "mon", "mes",
			"ta", "ton", "tes", "de", "du", "des", "au", "aux", "etc", "ce",
			"cet", "cette", "ceux", "celui", "celle", "ca", "pas", "rien",
			"aucun", ""]


def accentControl(oldStr):
	newStr = oldStr
	newStr = newStr.replace('à', 'a')
	newStr = newStr.replace("è", "e")
	newStr = newStr.replace("é", "e")
	newStr = newStr.replace("ù", "u")
	newStr = newStr.replace("ç", "c")
	newStr = newStr.replace("ï", "i")
	newStr = newStr.replace("ô", "o")
	newStr = newStr.replace("ê", "e")
	newStr = newStr.replace("â", "a")
	newStr = newStr.replace(".", "")
	newStr = newStr.replace(",", "")
	newStr = newStr.replace("\\", "")
	newStr = newStr.replace("œ", "o")
	return newStr


#print accentControl("Moààààncéf")

urls =[]
soups =[]
mots = []

for i in range(1,11):
    urls.append('https://fr.wiktionary.org/wiki/Wiktionnaire:10000-wp-fr-'+str(i)+'000')

for url in urls :
    pg = requests.get(url,verify=False)
    soups.append(BeautifulSoup(pg.content, "lxml"))

for soup in soups:
    mots.append(soup.find_all("div",{"id":"mw-content-text"}))
    
myfile = open("wiki.txt", "w")

for item in mots:
    for i in item:
        for j in i.find_all('ul'):
            for k in j.find_all('li'):
                for m in k.find_all('a'):
                	tmp = accentControl(m.text.encode('utf-8')).lower().strip()
                	if tmp not in delete_list:
                		myfile.write(tmp+'\n')

