from sklearn.datasets import *
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import BaggingClassifier
from nltk.stem import WordNetLemmatizer
import pandas as pd
import pickle

default_save_filename = "model.pkl"


def create(n_classes, n_features):
#    dataframe = pd.DataFrame({"text": {}, "testoutput": {}})
    classifier = BaggingClassifier()
    return classifier


def save(model, filename):
    with open(filename, "wb") as file:
        pickle.dump(model, file)

def load(filename):
    model = None
    with open(filename, "rb") as file:
        model = pickle.load(file)
    return model

def learn(model, data):
    model.fit(data.text, data.category)




lemmatizer = WordNetLemmatizer()
punctuation = "!?/[]{};:'\"\|-=_+,.<>()@#$%^&*"

def sanitize(text):
    text = text.replace("\n", " ")
    for forbidden in punctuation:
        text = text.replace(forbidden, "")

    vector = text.split()
    for j in range(len(vector)):
        vector[j] = lemmatizer.lemmatize(vector[j])
        
    text = " ".join(vector)
    return text


def vectorize(inputs, vectorizer):
    summaries_filtered = {}
    for i in inputs.index:
        text = inputs.text[i]
        summaries_filtered[i] = sanitize(text)
    inputs.update(pd.DataFrame({"text": summaries_filtered}))

    return vectorizer.fit_transform(inputs.text);
