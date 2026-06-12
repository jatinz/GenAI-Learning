'''
Stopwords
==========
These are the words like I, we, you, to etc which are to be removed from a corpus.

'''
import nltk
#nltk.download('stopwords')
#nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

#print(stopwords.words('english'))

corpus = """Lemmatization offers you a way to program an NLP algorithm using words
 morphologically rather than syntactically. In other words, via lemmatization, an NLP 
 algorithm understands words in and of themselves as discrete units 
 (including suffixes, prefixes, and inflections) rather than as parts of a sentence, 
 that accrue meaning with the addition of further words.
This modality is more straightforward for an NLP model to learn and build on. 
An NLP is a highly complex auto-correct feature, and it works by determining the 
statistical probability of a particular word following another. By breaking words
 down to lemmas—by discovering the root pattern of morphological inflection—an NLP 
 has fewer distinct words to learn. 
You can program an NLP more efficiently and accurately by working with simpler, 
more specific data—i.e., lemmas rather than chains of similar words differentiated by 
inflection. Such reduced training dimensionality improves tasks """

stemmer = SnowballStemmer('english')
sentences = nltk.sent_tokenize(corpus)
#print(sentences)

'''
In the below code: 
    - we are getting sentences from the corpus 
    - convert to word using word_tokenizer
    - get all the words that are not there in the stopwords
    - join the remaining words to the original sentence
'''
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentence = ' '.join(words)
    print(sentence)

