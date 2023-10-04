import pickle
import pandas as pd
from sklearn.datasets import *
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import BaggingClassifier
import nltk


dataframe = pd.DataFrame({"text": {}, "testoutput": {}})
x, y = make_multilabel_classification(n_classes = 1, random_state = 0)

classifier = MultiOutputClassifier(BaggingClassifier())
classifier.fit(x, y)

model_filename = "model.pkl"
with open(model_filename, "wb") as file:
    pickle.dump(classifier, file)

nltk.download("wordnet")
