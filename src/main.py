from sklearn.feature_extraction.text import *
import pickle
import fileinput
import pandas as pd
import numpy as np
import sklearn
import ui

import model

def split(input, training, testing):
    return sklearn.model_selection.train_test_split(
	    input, 
	    test_size=float(testing), train_size=float(training)
    )


vectorizer = CountVectorizer()
print(vectorizer)

classifier = model.create(n_classes = 5, n_features = 1)
print(classifier)

emails = pd.read_csv("emails.csv")







def print_screen(categories, email):
    ui.clear()
    ui.draw_categories(0, 0, 20, ui.height-15, categories)

    ui.set_bounds(20, 0, ui.width, ui.height)
    ui.draw_string(21, 1, ui.width-22, email)
    ui.draw_box(20, 0, ui.width-20, ui.height)

    ui.draw_categories(0, ui.height-15, 20, 15, ["Categorize", "New category", "Delete category"]);

    ui.draw()


categories = []
categories_sorted = {}
all_emails = []
categorized = []

def categorize_email(email, category): 
    try:
        title = categories[int(category)-1]
        categories_sorted[title].append(email)
    except:
        return

    print("Learning...")
    all_emails.append(email)
    categorized.append(int(category)-1)
    vectors = model.vectorize([email], vectorizer)
    data = {}
    data["text"] = all_emails
    data["category"] = categorized
    dataframe = pd.DataFrame(data=data)
    print(dataframe)


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




category_create("Work")
category_create("School")
category_create("Spam")
for email in emails.text:
    while True:
        print_screen(categories, email)
        selected = input("Select an action ")
        if selected == "1":
            print_screen(categories, email)
#            try:
            category = int(input("Place in folder "))
            if (category <= len(categories)):
                categorize_email(email, category)
                break; # Proceed to next email
#            except:
#                print("Failed to categorize")
#                selected = selected #omdat...
        elif selected == "2":
            print_screen(categories, email)
            name = (input("Create category "))
            category_create(name)
#            categories.append(name)
        elif selected == "3":
            print_screen(categories, email)
            category = int(input("Remove category "))
            if (category <= len(categories)):
                category_destroy(category)
#                categories.pop(int(category-1))


#model.save(classifier, model.default_save_filename)
