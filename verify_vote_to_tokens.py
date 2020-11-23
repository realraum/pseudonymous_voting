#!/usr/bin/python3

import csv
import secrets
import base64
import pprint
import random

tokenlen_short=3
tokenlen_full=tokenlen_short+2

tokensavailable = []
tokensused=[]

def indent_print(lst):
    for e in lst:
        print("\t"+e)
    print("")

with open("output_for_tp2_r3_fulltokens_only.csv","r") as csvtokensf:
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

with open("output_for_all_shorttokens_that_voted.csv","w+") as cout:
    cwst = csv.writer(cout)
    ## permutate list so identity can't be guessed from order in list (e.g. alphabetic ordered e-mails)
    used_shorttokens_list = [t.split("-")[0] for t in list(tokensused) if "-" in t and len(t)==11]
    random.shuffle(used_shorttokens_list)
    for tk in used_shorttokens_list:
        cwst.writerow([tk])

print("Tokens handed out BUT not yet used:")
indent_print(tokensavailable - tokensused)
print("Invalid Tokens appearing in vote:")
indent_print(tokensused - tokensavailable)