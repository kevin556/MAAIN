#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from sys import argv
	
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
		if i not in tmp and i not in delete_list:
			tmp.append(i)
	print tmp





if __name__ == '__main__':
	if len(argv) == 1:
		print("erreur aucun arguement pour la recherche")
	elif len(argv)> 10 : 
		print("erreur trop de mot pour la recherche")
	else:
		enleve_doublon(argv)
