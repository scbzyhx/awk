#! /usr/bin/env python

import re
import sys
import os

s= re.compile(r'[a-zA-Z0-9,{,},\[,\],(,),<,>,/,\\,=,;,\,:,.,\",\',\-,_,$,#,&,|,\*,+,`,\s,\n,!]*')

def func(f):
    
    ll = 0
    with open(f) as ff:
        for line in ff:
            line = line.strip("\n")
            ll = ll + len(s.sub('',line))
            #print s.sub('',line)
    return ll


if __name__ == "__main__":
    total = 0
    for filename in os.listdir(sys.argv[1]):
        filenames = filename.split('.')
        if len(filenames) > 1 and  filenames[1] == 'md':
            total = total + func(sys.argv[1] + '/'+filename)

    print total
