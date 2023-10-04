#!/usr/bin/python3

import random

class Figure:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)

class Line(Figure):
    pass

class Rect(Figure):    
    pass

class Ellipse(Figure):
    pass
    

elements = []    
for i in range (217):
    shape = random.randint(1,3)
    x1, y1 = random.randrange(0,1000), random.randrange(0,1000)
    x2, y2 = random.randrange(0,1000), random.randrange(0,1000)
    if shape == 1:
        elements.append(Line(x1, y1, x2, y2))
    elif shape == 2:
        elements.append(Rect(x1, y1, x2, y2))
    else:
        elements.append(Ellipse(x1, y1, x2, y2))


for i, val in enumerate(elements):
    if isinstance(val,Line):
        elements[i].sp = (0,0)
        elements[i].ep = (0,0)
    print("Element Nr {0}\tstart point {1}\tend point {2}\thas type {3}".format(i, elements[i].sp, elements[i].ep, type(elements[i])))
