#!/bin/python

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if x2 > x1:
    if v2 >= v1:
        print "NO"
        exit()

while True:
    x1 = x1+v1
    x2 = x2+v2
    if x2<x1:
        print "NO"
        exit()
    elif(x1 == x2):
        print "YES"
        exit()
    
    
