#!/usr/bin/env python
# coding: utf-8
import sys

def read_fasta (filename):
    seq=""
    f = open (filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            seq = seq + line
    f.close()
    return seq

if len(sys.argv) < 2:
    print ("Need to provide filename as argument")
    exit(1)

print (read_fasta(sys.argv[1]))

