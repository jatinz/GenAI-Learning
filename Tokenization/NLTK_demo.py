import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt_tab')

corpus = "Hello, My name is Jatin. I am learning Natural Language Processing with NLTK library."
sentences = nltk.sent_tokenize(corpus)
tokens = nltk.word_tokenize(corpus)
print("Sentences:")
print(sentences)
print("Tokens:")
print(tokens)
