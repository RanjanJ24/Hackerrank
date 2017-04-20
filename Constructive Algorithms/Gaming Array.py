#!/bin/python

import sys


g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    A = [int(i) for i in raw_input().split()]
    curr_max = -1
    count = 0
    for a in A:
        if a > curr_max:
            count += 1
            curr_max = a
    print "ANDY" if count % 2 == 0 else "BOB"
        
