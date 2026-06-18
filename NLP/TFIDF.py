'''
TFIDF : Term Frequencey - Inverse Document Frequence
-------------------------------------------------------

Term Frequency (TF) = No. of repeatation / No. of words in the sentence

IDF = log ( No. of sentences / No. of sentences containing the word)


s1 = "He is a good boy"
s2 = "she is a Good girl"
s3 = "Girl and boy are good "

Removing stopwords

s1 = "good boy"
s2 = "good girl"
s3 = "girl boy good"

Term Frequency:
-------------------------------------------------------------------------
    -No. of repeatation / No. of words in the sentence
-------------------------------------------------------------------------

        S1      S2      S3

good    1/2     1/2     1/3

boy     1/2     0       1/3 

girl    0       1/2     1/3


IDF:
-------------------------------------------------------------------------
    - log ( No. of sentences / No. of sentences containing the word)     
-------------------------------------------------------------------------

good    log(3/3) = 0    

boy     log(3/2) 

girl   log(3/2)

Now, TF-IDF means we need to multiply the TF of sentence 1 with all vocabulary,
so,
In S1:
 TF of "good" * IDF of "good" 
 TF of "boy" * IDF of "boy"
 TF of "girl" * IDF of "girl"

 and so on for S2 and S3 as well. So it will be :

        
        S1                          S2                          S3

good    1/2*0=0                   1/2*0=0                     1/3*0=0

boy     1/2*log(3/2)=0.203       0*log(3/2)=0                 1/3*log(3/2)=0.135

girl    0*log(3/2)=0             1/2*log(3/2)=0.203           1/3*log(3/2)=0.135


Advantages:
    - Easy to use
    - Importance of word is captured
    - weight of common words like "good" is kept low and important words are given 
        more weight 
    - Useful in search ranking, keyword extraction, spam detection, 
        text classification, and summarization

Disadvantages:
    - This technique which is mathematically called sparse metrics, can cause overfitting where,
        if case of many dataset, the metrics dimention increases too much.
    - Out of vocabulary : so if after training the model, if we give a sentence like :
        "Burger is bad", then the system would find that the word burger was not in the 
        matrix. So it won't be able to predict. 
    - Ordering of word changes.
    

'''