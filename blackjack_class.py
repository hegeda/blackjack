#!/usr/bin/python
# coding=utf-8
import os
import random
clear = lambda: os.system('clear')
vege = False
lapok = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'D': 10,
                 'K': 10, 'A': 11}

class Kartya(object):
    def __init__(self,kartyak):
        self.kartyak = kartyak

    def lap(self):
        kartya = random.choice(self.kartyak.items())
        return kartya

class Jatekos(object):
    def __init__(self, penz, tet, osszeg, lapok=[], ertek=[]):
        self.penz = penz
        self.tet = tet
        self.osszeg = osszeg
        self.lapok = lapok
        self.ertek = ertek

    def tetrakas(self):
        print 'Pénz: ', self.penz
        rak = input('Add meg a tétet: (min. 100)')
        self.tet = rak
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
        self.josszeg = josszeg
        self.oosszeg = oosszeg
        self.j_lapok = j_lapok
        self.o_lapok = o_lapok

    def j_rajzol(self):
        clear()
        print 'Pénz: ', self.penz
        print 'Tét: ', self.tet
        print 'Lapok', self.j_lapok
        #print 'összeg: ', josszeg

    def o_rajzol(self):
        clear()
        print 'Pénz: ', self.penz
        print 'Tét: ', self.tet
        print 'Lapok:', self.j_lapok
        #print 'összeg:', josszeg
        print 'Osztó:', self.o_lapok
        #print 'osztóösszeg: ', oosszeg

def ertekel():
    if jatekos.osszeg > 21:
        print 'Veszettél! A lapok összege: ', jatekos.osszeg
        tovabb()
        jatekvege()
    elif oszto.osszeg > 21:
        print 'Nyertél!'
        print 'Játékos lapjainak összege: ', jatekos.osszeg
        print 'Osztó lapjainak összege: ', oszto.osszeg
        jatekos.penz = jatekos.penz + 2 * jatekos.tet
        tovabb()
        jatekvege()
    elif 21 - jatekos.osszeg < 21 - oszto.osszeg:
        print 'Nyertél!'
        print 'Játékos lapjainak összege: ', jatekos.osszeg
        print 'Osztó lapjainak összege: ', oszto.osszeg
        jatekos.penz = jatekos.penz + 2 * jatekos.tet
        tovabb()
        jatekvege()
    else:
        print 'Veszettél! A lapok összege: ', jatekos.osszeg
        tovabb()
        jatekvege()

def tovabb():
    global vege
    valasz = raw_input("--tovább|q: kilép--")
    if valasz == 'q':
        if jatekos.penz > 0:
            print 'Nyeremény: ', jatekos.penz
            vege = True
            jatekvege()
        else:
            vege = True
            jatekvege()


def jatekvege():
    global vege
    if jatekos.penz == 0:
        vege = True

def init():
    clear()
    jatekos.lapok = []
    jatekos.ertek = []
    jatekos.osszeg = 0
    oszto.lapok = []
    oszto.ertek = []
    oszto.osszeg = 0


jatekos = Jatekos(1000, 0, 0, [])
oszto = Jatekos(0, 0, 0, [])
kartya = Kartya(lapok)


while not vege:
    init()
    tet = jatekos.tetrakas()

    if tet < 100:
        print 'Minimum 100!'
        tovabb()
        continue
    elif tet > jatekos.penz:
        print 'Nincs elég pénzed!'
        tovabb()
        continue
    else:
        jatekos.penz = jatekos.penz - jatekos.tet
        jatekos.lapothuz(kartya.lap())

    #asztal = Asztal(penz=jatekos.penz, tet=jatekos.tet, j_lapok=jatekos.lapok, o_lapok=oszto.lapok,j_laposszeg=sum(jatekos.lapok), o_laposszeg=sum(oszto.lapok))
    asztal = Asztal(penz=jatekos.penz, tet=jatekos.tet, josszeg=jatekos.osszeg, oosszeg=oszto.osszeg,
                    j_lapok=jatekos.lapok, o_lapok=oszto.lapok)
    #asztal.j_rajzol(jatekos.osszeg)
    asztal.j_rajzol()
    while jatekos.lapotker() == 'i':
        jatekos.lapothuz(kartya.lap())
        #asztal.j_rajzol(jatekos.osszeg)
        asztal.j_rajzol()
        if jatekos.osszeg > 21:
            break

    if jatekos.osszeg > 21:
        ertekel()
        continue

    oszto.lapothuz(kartya.lap())
    #asztal.o_rajzol(jatekos.osszeg, oszto.osszeg)
    asztal.o_rajzol()
    while oszto.osszeg <= 17:
        oszto.lapothuz(kartya.lap())
        #asztal.o_rajzol(jatekos.osszeg,oszto.osszeg)
        asztal.o_rajzol()
        if oszto.osszeg > 21:
            break
    ertekel()