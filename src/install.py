from sklearn.feature_extraction.text import *
from sklearn.ensemble import * 
import pandas as pd
import nltk

import model

nltk.download("wordnet")

classifier = model.create(n_classes = 5, n_features = 1)

vectorizer = CountVectorizer()
summaries = pd.read_csv("HilaryClintonEmails.csv")
features = model.vectorize(summaries, vectorizer)
vectors = vectorizer.transform(summaries.text)
classifier.fit(vectors, summaries.spam)


model.save(classifier, model.default_save_filename)
model.save(vectorizer, "vectorizer.pkl")

print("Installation succeeded")
