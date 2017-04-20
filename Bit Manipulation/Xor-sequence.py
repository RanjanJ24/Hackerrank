#!/bin/python

import sys

def B(X):
    if X % 8 == 0 or X % 8 == 1:
        return X
    elif X % 8 == 2 or X % 8 == 3:
        return 2
    elif X % 8 == 4 or X % 8 == 5:
        return X + 2
    else:
        return 0

Q = int(raw_input().strip())
for a0 in xrange(Q):
    L,R = map(long, raw_input().split())
    print B(L-1) ^ B(R)
    
