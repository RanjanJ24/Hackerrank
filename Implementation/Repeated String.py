#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
a = 0
for i in s:
    if i == 'a':
        a += 1
rem = n%len(s)
quo = n/len(s)
a = a * quo
for i in range(rem):
    if s[i] == 'a':
        a+=1
print a