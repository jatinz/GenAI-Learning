import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re 
from sklearn.feature_extraction.text import CountVectorizer

data = {
    "Message": [
        "Congratulations! You’ve won a free iPhone. Click here to claim your prize.",
        "Get cheap loans instantly. No credit check required. Apply now!",
        "Limited offer!!! Buy medicines at 70% discount. Visit our website today.",
        "You have been selected for a lottery. Send your bank details to receive funds.",
        "Hey, are we still meeting for lunch tomorrow?",
        "Don’t forget to bring the project report to class.",
        "Can you call me back when you’re free?",
        "The meeting has been rescheduled to 3 PM."
    ],
    "Label": ["Spam","Spam","Spam","Spam","Ham","Ham","Ham","Ham"]
}

ps = PorterStemmer()
df = pd.DataFrame(data)
cv = CountVectorizer(max_features=2500,binary=True,ngram_range=(1,3),stop_words='english')
x = cv.fit_transform(data.get("Message")).toarray()
print(cv.vocabulary_)