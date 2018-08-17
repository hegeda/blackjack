#!/usr/bin/python
# coding=utf-8
import os
import random
clear = lambda: os.system('clear')
vege = False

class Kartya(object):
    def __init__(self):
        pass
    def lap(self):
        lapok = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'D': 10,
                 'K': 10, 'A': 11}
        kartya = random.choice(lapok.items())
        return kartya

class Jatekos(object):
    def __init__(self, penz, tet, osszeg, lapok=[], ertek=[]):
        self.penz = penz
        self.tet = tet
        self.osszeg = osszeg
        self.lapok = lapok
        self.ertek = ertek

    def tetrakas(self):
        rak = input('Add meg a tétet: (min. 100)')
        self.tet=rak
        return self.tet

    def lapothuz(self,lap):
        self.lapok.append(lap[0])
        self.ertek.append(lap[1])
        self.osszeg=sum(self.ertek)

    def lapotker(self):
        valasz = raw_input("Kér lapot?: (i/n)")
        return valasz

class Asztal(object):
    def __init__(self, penz, tet, josszeg, oosszeg, j_lapok=[], o_lapok=[]):
        self.penz = penz
        self.tet = tet
        self.j_osszeg = josszeg
        self.o_osszeg = oosszeg
        self.j_lapok = j_lapok
        self.o_lapok = o_lapok

    def j_rajzol(self):
        clear()
        print 'Pénz: ', self.penz
        print 'Tét: ', self.tet
        print 'Lapok', self.j_lapok
        print 'összeg: ', self.j_osszeg

    def o_rajzol(self):
        clear()
        print 'Pénz: ', self.penz
        print 'Tét: ', self.tet
        print 'Lapok:', self.j_lapok
        print 'összeg:', self.j_osszeg
        print 'Osztó:', self.o_lapok
        print 'osztóösszeg: ', self.o_osszeg

def jatek():

    if osszeg_jatekos > 21:
        print 'Veszettél! A lapok összege: ', osszeg_jatekos
        jatekvege()
    elif 21 - osszeg_jatekos < 21 - osszeg_oszto:
        print 'Nyertél!'
        print 'Játékos lapjainak összege: ', sum(jatekos.lapok)
        print 'Osztó lapjainak összege: ', sum(oszto.lapok)
        jatekos.penz = jatekos.penz + 2 * jatekos.tet
    else:
        print 'Vesztettél!'
        print 'Játékos lapjainak összege: ', sum(jatekos.lapok)
        print 'Osztó lapjainak összege: ', sum(oszto.lapok)
        jatekvege()

def jatekvege():
    global vege
    if jatekos.penz == 0:
        vege = True


jatekos = Jatekos(1000, 0, 0, [])
oszto = Jatekos(0, 0, 0, [])
kartya = Kartya()
while not vege:
    jatekos.tetrakas()
    jatekos.lapothuz(kartya.lap())
    #asztal = Asztal(penz=jatekos.penz, tet=jatekos.tet, j_lapok=jatekos.lapok, o_lapok=oszto.lapok,j_laposszeg=sum(jatekos.lapok), o_laposszeg=sum(oszto.lapok))
    asztal = Asztal(penz=jatekos.penz,tet=jatekos.tet, josszeg=jatekos.osszeg, oosszeg=oszto.osszeg, j_lapok=jatekos.lapok,o_lapok=oszto.lapok)
    asztal.j_rajzol()
    if jatekos.lapotker() == 'n':
        oszto.lapothuz(kartya.lap())
        asztal.o_rajzol()


