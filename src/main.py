from sklearn.ensemble import *
from sklearn.neighbors import *
from sklearn.svm import *
from sklearn.tree import *
from sklearn.neural_network import *
from sklearn.naive_bayes import *
from sklearn.gaussian_process import *
from sklearn.discriminant_analysis import *
from sklearn.feature_extraction.text import *
from sklearn.linear_model import *
from sklearn.semi_supervised import *
import pickle
import fileinput
import pandas as pd
import numpy as np
import sklearn
import ui
import test

import model

def split(input, training, testing):
    return sklearn.model_selection.train_test_split(
	    input, 
	    test_size=float(testing), train_size=float(training)
    )


vectorizer = CountVectorizer()
classifier = model.create(n_classes = 5, n_features = 1)

emails = pd.read_csv("emails.csv")


vectorizers = [
    CountVectorizer,
#    HashingVectorizer,
#    TfidfVectorizer
]

#(gamma=2, C=1, random_state=42),

new_classifier = None
new_vectorizer = None

def newStackingClassifier():
    return RandomForestClassifier(n_estimators=100)


def newVotingClassifier():
    return VotingClassifier(estimators=100)



classifiers = [
    KNeighborsClassifier,
    RidgeClassifier,
    RidgeClassifierCV,
    SGDClassifier,
    SVC,
    MLPClassifier,
    AdaBoostClassifier, 
    BaggingClassifier, 
    ExtraTreesClassifier, 
    GradientBoostingClassifier, 
    IsolationForest,
    RandomForestClassifier,
    newStackingClassifier,
    DecisionTreeClassifier,
    ExtraTreeClassifier
]






categories = []
categories_sorted = {}
all_emails = []
categorized = []

test_results = []



test_num = 0


def write_tests():
    global vectorizer
    global classifier
    global new_vectorizer
    global new_classifier
    global test_num
    test.create_category("Religion")
    test.create_category("Politics")
    test.create_category("Spam")
    test.create_category("History")
    test.create_category("Discussion")
    test.categorize(1, False)
    test.categorize(2, False)
    test.categorize(3, False)
    test.categorize(3, False)
    test.categorize(2, False)
    test.categorize(1, False)
    test.categorize(1, False)
    test.categorize(4, False)
    test.categorize(2, False)
    test.categorize(2, False)
    test.skip()
    test.categorize(2, False)
    test.categorize(3, False)
    test.categorize(3, False)
    test.categorize(3, False)
    test.categorize(5, True)
    test.expect(3)
    test.expect(2)
    test.expect(2)
    test.expect(5)
    test.expect(2)
    

    x = test_num % len(vectorizers)
    y = int((test_num-x) / len(vectorizers))
    new_vectorizer = vectorizers[x]
    new_classifier = classifiers[y]
    vectorizer = new_vectorizer()
    classifier = new_classifier()
    print(vectorizer, classifier)
    test_num += 1
#    test.expect(
    test.report_results()
    test.reset()

write_tests()


def reset():
    global categories
    global categories_sorted
    global all_emails
    global categorized
    global test_results

    categories = []
    categories_sorted = {}
    all_emails = []
    categorized = []
    test_results = []
    write_tests()
  

def predict(email):
    global classifier
    global vectorizer

    vectorizer = new_vectorizer()
    all_emails.append(email)
    data = {}
    data["text"] = all_emails
    dataframe = pd.DataFrame(data=data)
    # Make sure the new features are supported
    model.sanitize_dataframe(dataframe)

    vectorizer.fit(dataframe.text)


    all_emails.pop()

    data = {}
    data["text"] = all_emails
    data["category"] = categorized
    dataframe = pd.DataFrame(data=data)

    
    model.sanitize_dataframe(dataframe)
    vectors = vectorizer.transform(dataframe.text)

    # Fit classifier to new features
    # Optimization: Don't do this if no new features are introduced
    classifier.fit(vectors, dataframe.category)

    data = {}
    data["text"] = [email]
    dataframe = pd.DataFrame(data=data)


    vectors = vectorizer.transform(dataframe)
    predicted = classifier.predict(vectors)
    return predicted[0]


def expect(email, folder):
    predicted = predict(email)
    test_results.append(predicted == folder)


def categorize_email_quick(email, category):
    try:
        title = categories[int(category)-1]
        categories_sorted[title].append(email)
    except:
        return


    all_emails.append(email)
    categorized.append(int(category)-1)


def categorize_email(email, category): 
    categorize_email_quick(email, category)

    
    data = {}
    data["text"] = all_emails
    data["category"] = categorized
    dataframe = pd.DataFrame(data=data)

    vectors = model.vectorize(dataframe, vectorizer)

    classifier = new_classifier()
    classifier.fit(vectors, dataframe.category)


def category_create(title):
    categories_sorted[title] = []
    categories.append(title)

def category_destroy(category):
    try:
        title = categories[int(category)-1]
        categories_sorted[title] = None
        categories.pop(category-1)
    except:
        return
    for email in email_categories:
        if email_categories[email] >= int(category):
            email_categories[email] -= 1
        elif email_categories[email] == int(category)-1:
            email_categories[email] = None

def print_screen(categories, email):
    if test.i < len(test.inputs):
        return
    ui.clear()
    ui.draw_categories(0, 0, 20, ui.height-15, categories)

    ui.set_bounds(20, 0, ui.width, ui.height-2)
    ui.draw_string(21, 1, ui.width-22, email)
    ui.set_bounds(20, 0, ui.width, ui.height)
    ui.draw_box(20, 0, ui.width-20, ui.height)

    print(categorized)
    if len(categorized) > 0:
        predicted = predict(email)
        #        ui.set_bounds()
        ui.draw_string(21, ui.height-2, ui.width-22, "Predicted: "+categories[predicted])

    ui.draw_categories(0, ui.height-15, 20, 15, ["Categorize", "New category", "Delete category", "Categorize quick", "skip", "reset", "expect"]);

    ui.draw()




def get_input(str):
    (succes, val) = test.read()
    if succes:
        return val
    return input(str)




i = 0
while i < len(emails.text):
    email = emails.text[i]
    i += 1
    while True:
        print_screen(categories, email)
        selected = get_input("Select an action ")
        if selected == "1":
            print_screen(categories, email)
            category = int(get_input("Place in folder "))
            if (category <= len(categories)):
                categorize_email(email, category)
                break; # Proceed to next email
        elif selected == "2":
            print_screen(categories, email)
            name = (get_input("Create category "))
            category_create(name)
        elif selected == "3":
            print_screen(categories, email)
            category = int(get_input("Remove category "))
            if (category <= len(categories)):
                category_destroy(category)
        elif selected == "4":
            print_screen(categories, email)
            category = int(get_input("Place in folder "))
            if (category <= len(categories)):
                categorize_email_quick(email, category)
                break; # Proceed to next email
        elif selected == "5":
            break;
        elif selected == "6":
            i = 0;
            reset()
            break;
        elif selected == "7":
            category = int(get_input("Expect in folder "))
            if (category <= len(categories)):
                expect(email, category)
                break;
        elif selected == "8":
            succesful = 0
            total = 0
            for result in test_results:
                if result:
                    succesful += 1
                total += 1
            print(succesful, total)
            print(succesful / total)
