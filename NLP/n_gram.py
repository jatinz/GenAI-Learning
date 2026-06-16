'''
s1 = The food is good
s2 = The food is not good

N-gram can be of types on the basis of how many consecutive words taken for vector:
    1. unigram
    2. bigram 
    3. trigram

For our example, 
    initial vocabulary -> food, not, good

    Using bigram:

        |----inital vector----| |-------------bigram-------------|
        food    not     good    food good   food not    not good
    S1  1       0       1           1           0           0   
    S2  1       1       1           0           1           1

    Now, we can see both vectors are clearly showing a lot of difference

    In sklearn, using (1,1) -> Unigram | (1,2) -> Unigram, bigram | 
        (1,3) -> Unigram, bigram and trigram, (2,3) -> bigram & trigram
'''