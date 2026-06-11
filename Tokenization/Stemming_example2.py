'''
Snowball Stemmer 
===================
The Snowball Stemmer is an improved, faster, and more advanced version of the Porter Stemmer
 that supports multiple languages and offers higher linguistic accuracy. Both algorithms
were created by Martin Porter, with Snowball (also known as the Porter2 stemmer) 
designed specifically to address the core flaws and limitations of his original
1980 Porter algorithm.Core DifferencesFeaturePorter StemmerSnowball Stemmer 
(Porter2)Language SupportEnglish onlyMultilingual (English, Spanish, German, French, etc.)
Speed & PerformanceStandardFaster and computationally 
optimizedAggressivenessGentle / ConservativeSlightly more aggressive and preciseStopwords 
HandlingCannot ignore stopwords nativelyCan ignore stopwords via parametersAccuracyProne to 
false conflations (e.g., fairly → fairli)Fixes major edge cases (e.g., fairly → fair)Key 
Improvements in SnowballBetter Rule Logic: Snowball addresses common logical errors in 
Porter, such as properly handling the suffix -ly. For instance, Porter stems 
happily to happili, whereas Snowball handles it more cleanly.
Special Case Exception Lists: Snowball explicitly protects distinct words that Porter 
mistakenly collapses into the same root. For example, Snowball recognizes that news is 
not the plural of new.Multilingual Framework: While the original Porter stemmer is hardcoded 
for English morphology, Snowball is actually a string-processing language 
designed to write stemming algorithms for many European languages
'''

from nltk.stem import SnowballStemmer

sbStemmer = SnowballStemmer('english')
words = ["running", "runner", "ran", "runs","eating", "eaten", "eats","writing", "written", "writes","history"]


for word in words:
    print(f"{word} --> {sbStemmer.stem(word)}")

'''
 
 Notice with the result, history is converted to histori
 Snowball stemming is an improvement to porter stemming, but still not the perfect one.
 Here comes lemmitization technique.

 '''
