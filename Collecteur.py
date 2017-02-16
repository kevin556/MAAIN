#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET

tmp = False
tmp2 = False
def process_buffer(buf):
    tnode = ET.fromstring(buf)
    #pull it apart and stick it in the database


mots = [line.rstrip('\n') for line in open('dictionnaire.txt')]
inputbuffer = ''
   
with open('frwiki-latest-stub-articles1.xml','rb') as inputfile:
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



