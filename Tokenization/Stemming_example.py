'''
Defination of Steming :
========================
Steming is the process of reducing a word to its base or root form called lemma. It is commonly 
used in natural language processing (NLP) tasks to improve the performance of algorithms by reducing 
the number of unique words in a text.

For example, the words "running", "runner", and "ran" can all be reduced to the stem "run". 
This helps algorithms to recognize that these words are related and can be treated as the 
same word in certain contexts.

Let's take an example of classification problem:

'''
from nltk.stem import PorterStemmer

words = ["running", "runner", "ran", "runs","eating", "eaten", "eats","writing", "written", "writes"]
ps = PorterStemmer()

for word in words:
    print(f"{word} --> {ps.stem(word)}")