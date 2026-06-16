'''

1. Lower case
2. Apply stopwords as words like he, she, is, a is not needed for sentiment analysis


s1 = "He is a good boy"
s2 = "she is a Good girl"
s3 = "Girl and boy are good "

Once stop word is implemented, the above is converted to :

s1 = "good boy"
s2 = "good girl"
s3 = "girl boy good"

Now, unique words : good boy girl

So vector : 

    good    boy     girl
s1 [ 1       1       0]
s2 [ 1       0       1]
s3 [ 1       1       1]

Now binary bag of word, only 1 and 0 is used but in bag of word, the number of occurance : n can
be used instead of just simple 1 and 0.

Advantages :
    - Simple to use
    - fixed size

Disadvantages :
    - This technique which is mathematically called sparse metrics, can cause overfitting where,
        if case of many dataset, the metrics dimention increases too much.
    - Ordering of word changes. So in matrix, in s3, the ordering was "girl boy good",
        but looking at the vector, s3 [ 1       1       1] , it is becoming, "good boy girl"
    - Out of vocabulary : so if after training the model, if any new word comes, then model
        won't be able to formulate the matrix.
    - No symantics meaning between words are getting captured. So we cannot say which word
        is more important or which word meaning is what.

------------------------------------------------------------------------------
    ** So the only difference from One hot encoding is the use of stop words 
------------------------------------------------------------------------------


'''