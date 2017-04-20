#!/bin/python
from __future__ import print_function
import sys
import math


s = raw_input().strip()
n = len(s)
row = math.floor(math.sqrt(n))
col = math.ceil(math.sqrt(n))
row = int(row)
col = int(col)
while (row*col < n):
    row += 1
    #col += 1

matrix = [[0 for i in xrange(row)] for j in xrange(col)]
character = 0
for i in xrange(row):
    for j in xrange(col):
        if(character < n):
            matrix[j][i] = s[character]
            character +=1       
#print (matrix)
for i in range(col):
    for j in range(row):
        if(matrix[i][j] != 0):
            print (matrix[i][j], end='')
    print (' ',end='')