#!/usr/bin/python

import math

pi = 3.1415

# input values of L and t from user

ui = input("enter value of t (thickness, gms, g/m2 of paper in milimeters): ")

t = ui

ui = input("now enter value of L (length (longer side) of paper in milimeters): ")

L = ui

print "if thickness of paper is:", t , "and length is:", L

# solve equation now

base = 2.718281828459

s1 = math.log(2, base)

d1 = 2 * t * math.sqrt(pi)

n1 = 25 * pi * (t * t)

n2 = 24 * t * L

n3 = n1 + n2

n4 = math.sqrt(n3)

n5 = (n4 / d1)

n6 = n5 - 0.66

nx = math.log(n6, base)

nz = nx / s1

n = uconv = int(nz)

print "than number of folds possible are:", n
