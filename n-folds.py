#!/usr/bin/python

import math

pi = 3.1415

# input values of W and t from user

ui = input("enter value of t (thickness, gms, g/m2 of paper in milimeters): ")

s1 = ui * pi

ui = input("now enter value of W (width of square paper in milimeters): ")

s2 = ui / s1

#calculate log base 2

x = ui / s1
base = 2

logof = math.log(x, base)

#calculate n : number of folds

m1 = 0.66 * logof

m2 = m1 + 1

m3 = uconv = int(m2)

print "number of folds possible are: ", m3
