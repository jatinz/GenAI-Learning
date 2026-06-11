'''
Wordnet Lemmitization
=============
It is like stemming but the output is called lemma and it is a root word rather than
a root stem.
NLTK provides WordNetLemmatizer wrapper class around wordnet corpus which uses morphy()
Unlike simpler methods, it analyzes grammar, context, and part-of-speech to ensure the 
output is an actual, meaningful word
Lemmatization looks at how a word functions within a specific sentence. It relies heavily 
on vocabularies, dictionaries (like WordNet), and morphological analysis to understand 
what a word means before trimming its affixes.
It is slower than stemming as it uses a dictionary to compare and get the lemma.

'''
from nltk.stem import WordNetLemmatizer
# import nltk
# nltk.download('wordnet')
'''
POS tag :
Noun - n
Verb - v
Adjective - a
Adverb - r
'''
wnLemmatizer = WordNetLemmatizer()
print(wnLemmatizer.lemmatize("going",pos='n')) #word will be treated as noun and hence printed as it is.
print(wnLemmatizer.lemmatize("going",pos='v')) #word will be treated as verb 

words = ["running", "runner", "ran", "runs","eating", "eaten", "eats","writing", "written", "writes","history"]


for word in words:
    print(f"{word} --> {wnLemmatizer.lemmatize(word,pos='v')}")