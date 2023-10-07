#!/usr/bin/python3

""" Analyzes three input arguments to see
if they can be sides of a triangle."""

import sys

class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.is_triangle() != 3:
            return "This is not a triangle"
        A = float(self.a)
        B = float(self.b)
        C = float(self.c)
        S = (A + B + C) / 2
        area = (S * (S-A) * (S-B) * (S-C))**0.5
        return "The area of the triangle is {:.3f}".format(area)

    def is_digits(self):
        if not (self.a.isdigit() and \
            self.b.isdigit() and self.c.isdigit()):
            return False
        return True

    def is_triangle(self):
        if not self.is_digits():
            return 1
        A = float(self.a)
        B = float(self.b)
        C = float(self.c)
        if A > (B + C) or B > (A + C) or C > (A + B):
            return 2
        elif A <= 0 or B <= 0 or C <= 0:
            return 2
        else:
            return 3

def input_check():
    if len(sys.argv) < 4:
        print("Please please enter the lengths of the three sides of the triangle")
        sys.exit(0)
    else:
        return sys.argv[1], sys.argv[2], sys.argv[3]


a, b, c = input_check()
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
print(tr)
