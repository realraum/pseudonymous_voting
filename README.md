# pseudonymous_voting r3 tries online voting with a low degree of privacy

- Right during CoViD19 we have a general assembly.
- Many members wish to vote anonymously, even if a trused online voting system cannot exist

So we try a bad approximation of somewhat private online voting

## The system

todo m1ch

## Usage of the scripts

### as TP1

1. choose a direct channel where you can reach your voters (e-Mail / DM)
2. generate a single-column csv list of voters (e-Mail or DM-Handle) and name it ```data/input_r3_voters_emails.csv```
3. call ```python3 token_gen.py```
4. check output ```data/output_for_tp1_tokens_for_r3_voters.csv``` and ```data/output_for_tp2_r3_fulltokens_only.csv```
5. send ONLY ```data/output_for_tp2_r3_fulltokens_only.csv``` to TP2
6. use ```data/output_for_tp1_tokens_for_r3_voters.csv``` to send each voter their token
7. publish ```data/output_for_all_shorttokens_allowed_to_vote.csv``` to members

### as TP2

1. save ```data/output_for_tp2_r3_fulltokens_only.csv``` you got from TP1 in this directory
2. download voting results from nuudle via admin link and CSV and name it ```data/r3votenuudel.csv```
3. call ```data/python3 verify_vote_to_tokens.py```
4. publish results from nuudle and metainfo from script (number of invalid tokens)
5. publish ```data/output_for_all_shorttokens_that_voted.csv``` to members


## The ideas behind the system

### Base assumptions

- TP1 has a direct channel to reach each individual voter
- TP2 has a broadcast channel to reach every voter BUT TP1

- TP1 and TP2 don't cooperate
- All voters will keep screenshot secret from TP1
- TP1 are trustworthy and check each other
- TP2 are several trustworthy people that check each other
- voters are not incompetent
- nuudle is useable and hidden votes are supported
- tokens can be sent privately
- nuudle does not care which voters connect's to it and keeps origin-ip of voter secret

- nobody knows wo is which token (except TP1)
  - TP1 will never see the nuudle result

- TP2 do not who which token is who so are inclined to treat all votes equally
- TP2 don't invent results

### Attacks and Checks

- TP1 could generate more tokens than voters and vote multiple times themselves
  - TP2s need to count number of tokens
  - voters need to check if their token is in list of short-tokens published by TP1 AND published by TP2
- TP1 could forget to send some people their tokens
  - voters need to complain if they did not get a token
  - TP2 must not start vote before everybody got a token
- TP2 could invent result instead of counting and announce invention
  - TP2 need to be trustworthy people with different agendas and check each other
  - possibly publish screenshot of admin-visible result to everyone BUT TP1, with the last part of the token painted over.
    - so every voter can check they were counted and that announced result still matches screenshot

