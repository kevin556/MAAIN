#!/usr/bin/python2.7
from random import randint

exemple={}

for i in range(0,10):
	exemple[i] = {i+1:i+2}
print exemple

print exemple[randint(0,len(exemple)-1)]