import pickle
import fileinput
import pandas as pd
import numpy as np
import sklearn

import model

def split(input, training, testing):
    return sklearn.model_selection.train_test_split(
	    input, 
	    test_size=float(testing), train_size=float(training)
    )


vectorizer = model.load("vectorizer.pkl")
print(vectorizer)

classifier = model.load(model.default_save_filename)
print(classifier)

print("Enter a line >")
for line in fileinput.input():
    print(line)
    vectors = vectorizer.transform(line)
    print(vectors)
    predicted = classifier.predict(vectors)
    print(predicted)
    print("Enter a line >")

#model.save(classifier, model.default_save_filename)



'''
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
'''
