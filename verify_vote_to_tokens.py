#!/usr/bin/python3

import csv
import secrets
import base64
import pprint

tokenlen_short=3
tokenlen_full=tokenlen_short+2

tokensavailable = []
tokensused=[]

def indent_print(lst):
    for e in lst:
        print("\t"+e)
    print("")

with open("output_for_tp2_r3_tokens_only.csv","r") as csvtokensf:
    ctokens = csv.reader(csvtokensf)
    for row in ctokens:
        assert(len(row)==1)
        assert("-" in row[0])
        tokensavailable += row

with open("r3votenuudel.csv","r") as csvvotesf:
            cvotes = csv.reader(csvvotesf)
            headers = next(cvotes)
            for row in cvotes:
                tokensused += [row[0].strip()]

tokensavailable=set(tokensavailable)
tokensused=set(tokensused)

print("Tokens handed out BUT not yet used:")
indent_print(tokensavailable - tokensused)
print("Invalid Tokens appearing in vote:")
indent_print(tokensused - tokensavailable)