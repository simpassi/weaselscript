#!/usr/bin/env python
import sys
import os
import random

if len(sys.argv) < 2:
    print("USAGE: weaselscript.py <input file>")
    sys.exit(1)

# look real closely
weasel_bits = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "　", "﻿"]
weasel_hisses = ["hiss", "hissss", "ssh", "sshk", "sk", "hsk", "shhh", "ss", "sss"]
weasel_header = "Weasel:"

if sys.argv[1] == "-test":
    for i, b in enumerate(weasel_bits):
        print("Bit {}: {}".format(i,ord(b)))
    sys.exit(0)

def weaselcode(b):
    b1 = ord(b) >> 4
    b2 = ord(b) & 0xf
    return weasel_bits[b1], weasel_bits[b2]

def weaseldecode(b1, b2):
    return b1 << 4 | b2

def hiss():
    return random.choice(weasel_hisses)

line_width = int(os.environ.get("WEASEL_LINE_WIDTH", "120"))

idx = 0
decode = False
with open(sys.argv[1], "rb") as f:
    try:
        if str(f.read(7), "utf-8") == weasel_header:
            decode = True
    except:
        pass

if decode:
    with open(sys.argv[1], "r") as f:
        halfbits = []
        lne = f.readline()
        while lne:
            for c in lne:
                if c in weasel_bits:
                    halfbits.append(weasel_bits.index(c))
                    if len(halfbits) == 2:
                        sys.stdout.buffer.write(bytes([weaseldecode(halfbits[0], halfbits[1])]))
                        halfbits = []
            lne = f.readline()
        
else:
    with open(sys.argv[1], "rb") as f:
        sys.stdout.write(weasel_header)
        idx+=7
        c = f.read(1)
        while c:
            b1, b2 = weaselcode(c)
            w1, w2 = hiss(), hiss()
            sys.stdout.write("{}{}{}{}".format(b1, w1, b2, w2))
            c = f.read(1)
            idx += 2 + len(w1) + len(w2)
            if line_width > 0 and idx > line_width - 2:
                idx = 0
                sys.stdout.write("\n")
        sys.stdout.write("!\n")
