#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
# your code goes here
count = 0
if k >= max(height):
    print 0
    exit()
for val in height:
    if k < val:
        dif = val - k
        count = count + dif
        k = k + dif
print count