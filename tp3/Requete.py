#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from sys import argv
import xml.etree.cElementTree as ET


delete_list = ["et","le", "la", "les",
			"un", "une", "a", "en", "sa", "son", "ses", "ma", "mon", "mes",
			"ta", "ton", "tes", "de", "du", "des", "au", "aux", "etc", "ce",
			"cet", "cette", "ceux", "celui", "celle", "ca", "ça", "pas", "rien",
			"aucun", ""]



def enleve_doublon(source):
	tmp=[]
	'''
		source[1:] -> pour ne pas avoir le nom de l'executable dans le tableau de sortie
	'''
	for i in source[1:]:
		#and not i.isdigit():
		if i not in tmp and i not in delete_list :
			tmp.append(i.lower())
	return tmp

'''
	conception algo:
		parcours du fichier a la recherche des mots de la requete.
		on repere le mot a droite:
			si ça correspond,on stocke les ids des pages dans lequel le premier mot apparait.
		on parcoure a nouveau le fichier a la recherche du ou des autres mots.
			une fois trouvé on enleve les mots qui n'apparaissent pas dans la seconde liste.
			Pour les mots apparaissant plusieurs fois,on ajoute les apparitions des deux pages
			dans le tableau res et on trie par rapport à cette fréquence.

'''

def algo_recherche(source,fichier_graphe):
	dico_temp ={}
	print "source %s"%(source)
	
	for motrecherche in source:
	    context = ET.iterparse(fileName, events=("start", "end"))
	    context = iter(context)
	    event, root = context.next()
	    for event, elem in context:
	        if event == "end" and elem.tag == "mot":
	            mot = elem.findtext("contenu").encode('utf-8')
	            if mot == motrecherche:
	              	for page in elem.iter('page'):
	                	print page.attrib['id'] + " " + elem.findtext("page")




if __name__ == '__main__':
	if len(argv) == 1:
		print("erreur aucun arguement pour la recherche")
	elif len(argv)> 10 : 
		print("erreur trop de mot pour la recherche")
	else:
		algo_recherche(enleve_doublon(argv),"/Users/kevin/Desktop/graph_maain/graph_granola.txt")