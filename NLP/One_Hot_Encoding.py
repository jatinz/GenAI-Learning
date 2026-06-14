'''
One Hot encoding
==================
Technique to convert the text to vector

Lets take an example

D1 = The Food is great
D2 = The food is bad
D3 = pizza is amazing

Unique words between D1, D2 and D3 :

    -> The 	food	is	   good	    bad	    pizza	amazing

Representation of all the sentences as vectors :

		    The 	food	is	   good	    bad	    pizza	amazing
D1	The	    1	    0	    0	    0	      0	        0	    0
	Food	0	    1	    0	    0	      0	        0	    0
	is	    0	    0	    1	    0	      0	        0	    0
	good	0	    0	    0	    1	      0	        0	    0
								
D2	The	    1	    0	    0	    0	      0	        0	    0
	Food	0	    1	    0	    0	      0	        0	    0
	is	    0	    0	    1	    0	      0	        0	    0
	bad	    0	    0	    0	    0	      1	        0	    0
								
D3	pizza	0	    0	    0	    0	      0	        1	    0
	is	    0	    0	    1	    0	      0	        0	    0
	amazing	0	    0	    0	    0	      0	        0	    1

So Vector would be :

[1,0,0,0,0,0,0]   # The
[0,1,0,0,0,0,0]   # Food
[0,0,1,0,0,0,0]   # is
[0,0,0,1,0,0,0]   # good

[1,0,0,0,0,0,0]   # The
[0,1,0,0,0,0,0]   # Food
[0,0,1,0,0,0,0]   # is
[0,0,0,0,1,0,0]   # bad

[0,0,0,0,0,1,0]   # pizza
[0,0,1,0,0,0,0]   # is
[0,0,0,0,0,0,1]   # amazing


Advantage:
    - Easy to implement in python. Libraries sklearn:oneHotEncoader, pandas : pd.get_dummies()

Disadvantages:
    - This technique which is mathematically called sparse metrics, can cause overfitting where,
        if case of many dataset, the metrics dimention increases too much.
    - Size difference, notice in the D3, the matrix is 3x7 and not 4x7 like others. So this
        difference would cause issue which training LLM.
    - No symantics meaning between words are getting captured. So we cannot say which word
        is more important or which word meaning is what.
    - Out of vocabulary : so if after training the model, if we give a sentence like :
        "Burger is bad", then the system would find that the word burger was not in the 
        matrix. So it won't be able to predict. 
'''