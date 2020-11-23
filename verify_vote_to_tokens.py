#!/usr/bin/python3

import csv
import os
import secrets
import base64
import pprint
import random
import datetime

tokenlen_short=3
tokenlen_full=tokenlen_short+2

tokensavailable = []
tokensused=[]

def indent_print(lst):
    for e in lst:
        print("\t"+e)
    print("")

with open("./data/output_for_tp2_r3_fulltokens_only.csv","r") as csvtokensf:
    ctokens = csv.reader(csvtokensf)
    for row in ctokens:
        assert(len(row)==1)
        assert("-" in row[0])
        tokensavailable += row

vote_results_filename = "./data/r3votenuudel.csv"
utimestamp_vote_results = os.path.getmtime(vote_results_filename)
with open(vote_results_filename,"r") as csvvotesf:
            cvotes = csv.reader(csvvotesf)
            headers = next(cvotes)
            for row in cvotes:
                tokensused += [row[0].strip()]

tokensavailable=set(tokensavailable)
tokensused=set(tokensused)

with open("./data/output_for_all_shorttokens_that_voted.csv","w+") as cout:
    cwst = csv.writer(cout)
    ## permutate list so identity can't be guessed from order in list (e.g. alphabetic ordered e-mails)
    used_shorttokens_list = [t.split("-")[0] for t in list(tokensused) if "-" in t and len(t)==11 and t in tokensavailable]
    random.shuffle(used_shorttokens_list)
    for tk in used_shorttokens_list:
        cwst.writerow([tk])

asofyet_unused_tokens = tokensavailable - tokensused
unrecognized_tokens_in_vote = tokensused - tokensavailable

print("Stats that all are allowed to see:")
print("\tNumber of as-of-yet(%s) unused tokens: %d" % (datetime.datetime.fromtimestamp(utimestamp_vote_results).strftime("%F %T%z"),len(asofyet_unused_tokens)))
print("\tNumber of votes with unrecognized token: %d" % (len(unrecognized_tokens_in_vote)))
print("")

print("Tokens handed out BUT not yet used:")
indent_print(asofyet_unused_tokens)
print("Unrecognized Tokens appearing in vote:")
indent_print(unrecognized_tokens_in_vote)