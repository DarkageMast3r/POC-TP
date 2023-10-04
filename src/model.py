from sklearn.datasets import *
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import BaggingClassifier
import pickle

default_save_filename = "model.pkl"


def create(n_classes):
#    dataframe = pd.DataFrame({"text": {}, "testoutput": {}})
    classifier = MultiOutputClassifier(BaggingClassifier())
    x, y = make_multilabel_classification(
        n_classes = n_classes,
        random_state = 0
    )
    classifier.fit(x, y)
    return classifier


def save(model, filename):
    with open(filename, "wb") as file:
        pickle.dump(model, file)

def load(filename):
    model = nil
    with open(filename, "rb") as file:
        model = pickle.load(file)
    return model
