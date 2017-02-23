#!/usr/bin/python2.7
from random import randint

#structure mot-page

d = {'mot1': {'idpage1': 1, 'idpage1': 2}, 'mot2': {'idpage1': 3, 'idpage2': 4}}

#l'access  aux elements se fait comme suit ...

print d['mot1']           # {'idpage1': 1, 'idpage1': 2}
print d['mot1']['idpage1']    # 1
print d['mot2']['idpage1']   # 3


#l'ajout d'element one by one

d['mot3'] = {}
d['mot3']['idpage1'] = 7
d['mot3']['idpage2'] = 8

d['mot2']['idpage1'] += 1


d['mot6'] = {}
d['mot6']['idpagex'] = 10
print d