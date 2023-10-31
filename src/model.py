from sklearn.datasets import *
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import BaggingClassifier
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import pickle

default_save_filename = "model.pkl"


def create(n_classes=0, n_features=0):
#    dataframe = pd.DataFrame({"text": {}, "testoutput": {}})
    classifier = BaggingClassifier()
    return classifier





lemmatizer = WordNetLemmatizer()
punctuation = "!?/[]{};:'\"\|-=_+,.<>()@#$%^&*"

def sanitize(text):
    text = text.replace("\n", " ")
    for forbidden in punctuation:
        text = text.replace(forbidden, "")

    vector = text.split()
    for j in range(len(vector)):
        vector[j] = lemmatizer.lemmatize(vector[j])
        
    stop_words = set(stopwords.words('english'))  # or any other language
    vector = [word for word in vector if word not in stop_words]

    text = " ".join(vector)
    return text

def sanitize_dataframe(inputs):
    summaries_filtered = {}
    for i in inputs.index:
        text = inputs.text[i]
        summaries_filtered[i] = sanitize(text)
    inputs.update(pd.DataFrame({"text": summaries_filtered}))

def vectorize(inputs, vectorizer):

    return vectorizer.fit_transform(inputs.text);
