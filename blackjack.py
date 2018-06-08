#!/usr/bin/python
# coding=utf-8
import os
import random

kartyak = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J': 10,'D': 10,'K': 10,'A': 11}
vege = False

class Jatekos(object):
        def __init__(self,penz,lapok=[]):
                self.penz = penz
                self.lapok = lapok


class Oszto(object):
        def __init__(self, penz, lapok=[]):
                self.lapok = lapok

def ertekel():
        global vege
        osszeg_jatekos = sum(jatekos.lapok)
        osszeg_oszto = sum(oszto.lapok)
        if osszeg_jatekos > 21:
                print 'Veszettél! A lapok összege: ', osszeg_jatekos
                vege = True
        elif 21-osszeg_jatekos < 21-osszeg_oszto:
                print 'Nyertél!'
                print 'Játékos lapjainak összege: ', sum(jatekos.lapok)
                print 'Osztó lapjainak összege: ', sum(oszto.lapok)
                exit()
        else:
                 print 'Vesztettél!'
                 print 'Játékos lapjainak összege: ', sum(jatekos.lapok)
                 print 'Osztó lapjainak összege: ', sum(oszto.lapok)
                 exit()


def lapotker():
        re = raw_input("Kér lapot?: (i/n)")
        if re == 'i':
                jatek()
        elif re == 'n':
                osztohuz()
        else:
                print 'i/n'
                lapotker()


def osztolapker():
        if sum(oszto.lapok) > 21:
                print 'Nyertél!'
                print 'Játékos lapjainak összege: ', sum(jatekos.lapok)
                print 'Osztó lapjainak összege: ', sum(oszto.lapok)
                exit()
        elif sum(oszto.lapok) > 17:
                ertekel()
        else:
                osztohuz()

def jatek():
        lap = random.choice(kartyak.items())
        jatekos.lapok.append(lap[1])
        print lap[0]
        print jatekos.lapok
        if sum(jatekos.lapok) > 21:
                print 'Veszettél! A lapok összege: ', sum(jatekos.lapok)
                exit()

        lapotker()

def osztohuz():
        osztolap = random.choice(kartyak.items())
        oszto.lapok.append(osztolap[1])
        print osztolap[0]
        print oszto.lapok
        osztolapker()

while not vege:
        jatekos = Jatekos(1000)
        oszto = Oszto(0)
        jatek()
