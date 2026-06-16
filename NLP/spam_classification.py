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
cv = CountVectorizer(max_features=2500)
#print(df)
# Initialize CountVectorizer
vectorizer = CountVectorizer()
corpus = ""

for msg in data.get("Message"):
    review = re.sub('[^a-zA-Z0-9]',' ',msg).lower().split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    print(f"-> {review}")