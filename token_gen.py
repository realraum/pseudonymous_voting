#!/usr/bin/python3

import csv
import secrets
import base64
import random

tokenlen_short=3
tokenlen_full=tokenlen_short+2

tokens_short = []
tokens_full = []

def genToken():
    global tokens_short, tokens_full
    tokennotfound = True
    x=bytes([0])
    xy=bytes([0])
    while tokennotfound:
        x=base64.b16encode(secrets.token_bytes(tokenlen_short))
        y=base64.b16encode(secrets.token_bytes(tokenlen_full-tokenlen_short))
        xy=x.decode("utf8")+"-"+y.decode("utf8")
        tokennotfound = x in tokens_short or xy in tokens_full if len(xy) != 11 ## ensure tokens are unique and of len 11
    tokens_short += [x]
    tokens_full += [xy]
    return xy

with open("input_r3_voters_emails.csv") as cf:
    with open("output_for_tp1_tokens_for_r3_voters.csv","w+") as cout:
            cs = csv.reader(cf)
            cwet = csv.writer(cout)
            for row in cs:
                newrow = [row[0],genToken()]
                cwet.writerow(newrow)

with open("output_for_tp2_r3_fulltokens_only.csv","w+") as cout:
    cwt = csv.writer(cout)
    ## permutate list so identity can't be guessed from order in list (e.g. alphabetic ordered e-mails)
    random.shuffle(tokens_full)
    for tk in tokens_full:
        cwt.writerow([tk])

with open("output_for_all_shorttokens_allowed_to_vote.csv","w+") as cout:
    cwst = csv.writer(cout)
    ## permutate list so identity can't be guessed from order in list (e.g. alphabetic ordered e-mails)
    random.shuffle(tokens_short)
    for tk in tokens_short:
        cwet.writerow([tk])

