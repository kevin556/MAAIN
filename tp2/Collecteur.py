#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from sys import argv
from Dictionnaire import get_word_file

tmp = False
tmp2 = False
mots = []

def process_buffer(buf):
    tnode = ET.fromstring(buf)
    #pull it apart and stick it in the database


def import_dico():
    mots = [line.rstrip('\n') for line in open('dictionnaire.txt')]


def do_the_harlem_shake(fileName):
    #Moncef pense que ça ne plantera pas
    tmp =False;tmp2=False
    with open(fileName,'rb') as inputfile:
        inputbuffer=""
        for line in inputfile:
            if '<page>' in line:
                #on entre dans la page
                tmp = True
            if tmp:
                #on est dans la page
                if '<title>' in line and '</title>' in line:
                    inputbuffer+=line.replace("<title>","").replace("</title>","").strip()
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
                print "inputbuffer %s" %(inputbuffer)
                break
                inputbuffer =""
                tmp = False
            
if __name__ == '__main__':
    if len(argv) == 2 :
        import_dico()
        do_the_harlem_shake(argv[1])
    else:
        print "mauvais nombre d'arguments\nusage ./Collecteur filename"


'''
    append = False
    for line in inputfile:
        if '<page>' in line:
            tmp = True
        if tmp:
            if '<titre>' in line:
                inputbuffer = line
            if '<text>' in line:
                tmp2 =True
            if tmp2:
                inputbuffer += line
            print "la %s" %(inputbuffer) 
            append = True
        elif '</page>' in line:
            print inputbuffer
            tmp = False
            tmp2 = False
            inputbuffer += line
            append = False
            process_buffer(inputbuffer)
            inputbuffer = None
            del inputbuffer #probably redundant...
        elif append:
            inputbuffer += line



'''