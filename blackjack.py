#!/usr/bin/python
# coding=utf-8
import os
import random

lapok = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J': 10,'D': 10,'K': 10,'A': 11}
vege = False
osszeg = 0

class Jatekos(object):
	def __init__(self,penz,lapok={}):
		self.penz=penz
		self.lapok=lapok
	
	def megall(self,stop):
		self.stop = stop
		stop = False
		return stop
	
def ertekel():
	if osszeg > 21:
		print 'Veszettél! A lapok összege: ', osszeg 		
	jatek()

def jatek():
	jatekos = Jatekos(1000)
	lap = random.choice(lapok.items())
	jatekos.lapok.append(random.choice(lap.values()))
	print lap.keys
 	for i in jatekos.lapok:
		ossz=ossz+i
	ertekel()	

while not vege:
	jatek()
