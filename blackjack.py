#!/usr/bin/python
# coding=utf-8
import os
import random

kartyak = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J': 10,'D': 10,'K': 10,'A': 11}
vege = False

class Jatekos(object):
	def __init__(self,penz,lapok=[]):
		self.penz=penz
		self.lapok=lapok
	
	def megall(self,stop):
		self.stop = stop
		stop = False
		return stop
	
def ertekel():
	global vege
	if sum(jatekos.lapok) > 21:
		print 'Veszettél! A lapok összege: ', sum(jatekos.lapok)
		vege = True
	else:
		jatek()

def jatek():
	lap = random.choice(kartyak.items())
	jatekos.lapok.append(lap[1])
	print lap[0]
	ertekel()	

while not vege:
	jatekos = Jatekos(1000)
	jatek()
