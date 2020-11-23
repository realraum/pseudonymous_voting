#!/usr/bin/python3

import csv
import secrets
import base64

tokenlen_short=3
tokenlen_full=tokenlen_short+2

tokensx = []
tokensxy = []

def genToken():
    global tokensx, tokensxy
    tokennotfound = True
    x=bytes([0])
    xy=bytes([0])
    while tokennotfound:
        x=base64.b16encode(secrets.token_bytes(tokenlen_short))
        y=base64.b16encode(secrets.token_bytes(tokenlen_full-tokenlen_short))
        xy=x.decode("utf8")+"-"+y.decode("utf8")
        tokennotfound = x in tokensx or xy in tokensxy ## ensure tokens are uniqe
    tokensx += [x]
    tokensxy += [xy]
    return xy

with open("input_r3_voters_emails.csv") as cf:
    with open("output_for_tp1_tokens_for_r3_voters.csv","w+") as cout:
        with open("output_for_tp2_r3_tokens_only.csv","w+") as cout:
            cs = csv.reader(cf)
            cwet = csv.writer(cout)
            cwt = csv.writer(cout)
            for row in cs:
                newrow = [row[0],genToken()]
                cwet.writerow(newrow)
                cwt.writerow([newrow[1]])

