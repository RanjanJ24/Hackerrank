#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())
ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6:'sixty'}
after_ten = {10:"ten",11: "eleven",12: "twelve",13: "thirteen",14: "fourteen",15: "fifteen",16: "sixteen",17: "seventeen",18: "eighteen",19: "nineteen"};
if m == 0:
    hr = str(h)
    if hr == '10' or hr == '11' or hr == '12':
        hr = after_ten[int(hr)]
    else:
        hr = int(hr)
        hr = ones[hr]
    print hr + " o' clock"
elif m == 1:
    #mit == str(m)
    hr = str(h)
    if hr == '10' or hr == '11' or hr == '12':
        hr = after_ten[int(hr)]
    else:
        hr = int(hr)
        hr = ones[hr]
    print "one minute past " + hr
elif m > 1 and m < 30 and m != 15:
    mit = str(m)
    hr = str(h)
    if hr == '10' or hr == '11' or hr == '12':
        hr = after_ten[int(hr)]
    else:
        hr = int(hr)
        hr = ones[hr]
    if m > 1 and m <10:
        mit = ones[m]
    elif m >= 10 and m <20:
        mit = after_ten[m]
    elif mit[1] == '0':
        mit = tens[m]
    else:
        ten = mit[0]
        one = mit[1]
        mit = tens[int(ten)] + " " + ones[int(one)]
    print mit + ' minutes past ' + hr
elif m == 15:
    hr = str(h)
    if hr == '10' or hr == '11' or hr == '12':
        hr = after_ten[int(hr)]
    else:
        hr = int(hr)
        hr = ones[hr]
    print "quarter past " + hr
elif m == 30:
    hr = str(h)
    if hr == '10' or hr == '11' or hr == '12':
        hr = after_ten[int(hr)]
    else:
        hr = int(hr)
        hr = ones[hr]
    print "half past " + hr
elif m > 30 and m < 60 and m != 45:
    mit = str(m)
    hr = str(h)
    if hr == '10' or hr == '11':
        hr = after_ten[int(hr)+1]
    elif  hr == '12':
        hr = ones[1]
    else:
        hr = int(hr) + 1
        hr = ones[hr]
    m = 60 - m
    mit = str(m)
    if m > 1 and m <10:
        mit = ones[m]
    elif m >= 10 and m <20:
        mit = after_ten[m]
    elif mit[1] == '0':
        mit = tens[m]
    else:
        ten = mit[0]
        one = mit[1]
        mit = tens[int(ten)] + " " + ones[int(one)]
    print mit + " minutes to " + hr  
elif m == 45:
    hr = str(h)
    if hr == '10' or hr == '11':
        hr = after_ten[int(hr)+1]
    elif  hr == '12':
        hr = ones[1]
    else:
        hr = int(hr) + 1
        hr = ones[hr]
    print "quarter to " + hr