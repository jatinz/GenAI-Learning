import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Your dataset
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

df = pd.DataFrame(data)

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the messages
X = vectorizer.fit_transform(df["Message"])

# Convert to DataFrame for readability
tfidf_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

print(tfidf_df.head())
