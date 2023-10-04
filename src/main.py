import pickle
import fileinput
import pandas as pd
import numpy as np
from nltk.stem import WordNetLemmatizer

import sklearn
from sklearn.ensemble import * 
from sklearn.feature_extraction.text import *


lemmatizer = WordNetLemmatizer()
punctuation = "!?/[]{};:'\"\|-=_+,.<>()@#$%^&*"

summaries = pd.read_csv("emails.csv")

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


def split(input, training, testing):
    return sklearn.model_selection.train_test_split(
	input, 
	test_size=float(testing), train_size=float(training))


training, testing = split(summaries, 0.8, 0.1)

vectorizer = CountVectorizer();
#classifier = BaggingClassifier();
features = vectorize(summaries, vectorizer);

classifier = model.load(model.default_save_filename)


vectors_training = vectorizer.transform(training.text)
classifier.fit(vectors_training, training.spam)

message = "> Enter an e-mail:"
email = ""

print(message)
for line in fileinput.input():
    if line == "\n":

        try:
            vector = vectorizer.transform([email])
            predicted = classifier.predict(vector);
            if predicted[0] == 0:
                print("Not spam!")
            else:
                print("Spam.")
        except:
            print("Could not parse input!");
        print(message)
        email = "";
    else:
        email = email + line;
