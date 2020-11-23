# pseudonymous_voting r3 tries online voting with a low degree of privacy

- Right during CoViD19 we have a general assembly.
- Some members which to vote anonymously even if a trused online voting system cannot exist

So we try a bad approximation of somewhat private online voting

## The system

todo m1ch

## Usage of the scripts

### as TP1

1. choose a direct channel where you can reach your voters (e-Mail / DM)
2. generate a single-column csv list of voters (e-Mail or DM-Handle) and name it ```input_r3_voters_emails.csv```
3. call ```python3 token_gen.py```
4. check output ```output_for_tp1_tokens_for_r3_voters.csv``` and ```output_for_tp2_r3_fulltokens_only.csv```
5. send ONLY ```output_for_tp2_r3_fulltokens_only.csv``` to TP2
6. use ```output_for_tp1_tokens_for_r3_voters.csv``` to send each voter their token
7. publish ```output_for_all_shorttokens_allowed_to_vote.csv``` to members

### as TP2

1. save ```output_for_tp2_r3_fulltokens_only.csv``` you got from TP1 in this directory
2. download voting results from nuudle via admin link and CSV and name it ```r3votenuudel.csv```
3. call ```python3 verify_vote_to_tokens.py```
4. publish results from nuudle and script
5. publish ```output_for_all_shorttokens_that_voted.csv``` to members


## The ideas behind the system
