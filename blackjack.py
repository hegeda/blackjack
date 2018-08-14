#!/usr/bin/python
# coding=utf-8
import os
import random

kartyak = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'D': 10, 'K': 10, 'A': 11}
vege = False
indulopenz = 1000


class Jatekos(object):
    def __init__(self, penz, tet, lapok=[]):
        self.penz = penz
        self.tet = tet
        self.lapok = lapok


def jatekvege():
    global vege
    print jatekos.penz, 'jatekvege'
    if jatekos.penz == 0:
        vege = True

def ertekel():
    global vege
    osszeg_jatekos = sum(jatekos.lapok)
    osszeg_oszto = sum(oszto.lapok)

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
        jatekvege()next

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
        jatekos.penz = jatekos.penz + 2 * jatekos.tet
    elif sum(oszto.lapok) > 17:
        ertekel()
    else:
        osztohuz()


def jatek():
    lap = random.choice(kartyak.items())
    jatekos.lapok.append(lap[1])
    print 'Pénz: ', jatekos.penz
    print 'Tét: ', jatekos.tet
    print lap[0]
    print jatekos.lapok
    if sum(jatekos.lapok) > 21:
        ertekel()
    else:
        lapotker()


def osztohuz():
    osztolap = random.choice(kartyak.items())
    oszto.lapok.append(osztolap[1])
    print osztolap[0]
    print oszto.lapok
    osztolapker()


def tetrakas():
    oszto.lapok = []
    jatekos.lapok = []
    print 'Pénz: ', jatekos.penz
    rak = input('Add meg a tétet: (min. 100)')
    if rak < 100:
        print 'Minimum tét: 100'
    elif rak > jatekos.penz:
        print 'Nincs elég pénzed'
    else:
        jatekos.tet = rak
        jatekos.penz = jatekos.penz - jatekos.tet
        jatek()

jatekos = Jatekos(indulopenz, 0, [])
oszto = Jatekos(0, 0, [])

while not vege:
    tetrakas()
