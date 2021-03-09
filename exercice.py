#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Exercice 5 notes de cours

# TODO: Importez vos modules ici
from math import pi
import sys
sys.path.insert(0, "C:\GitHub\INF-1007\Exercices classe\\2021h-ch6-1-exercices-KinanToutoungy")
from exercice_ch6 import frequence

import random
from turtle import *

# TODO: Définissez vos fonction ici

def masse_elipsoide(a=1,b=2,c=3, p=10):
    V = (4/3)*pi*a*b*c
    masse = p*V
    print(V, masse)
    return V, masse

def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)

def draw_tree():

    color("green")
    setheading(90)
    draw_branch(70, 7, 35)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    masse_elipsoide()
    masse_elipsoide(5,7,8,12)

    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("test test tests test"))
    draw_tree()