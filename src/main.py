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


vectorizer = model.load("vectorizer.pkl")
print(vectorizer)

classifier = model.load(model.default_save_filename)
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

def categorize_email(email, category):
    title = categories[category]
    categories_sorted[title].append(email)
    print(categories_sorted)
#    print(email, category)

def category_create(title):
    categories_sorted[title] = []
    categories.append(title)

def category_destroy(category):
    title = categories[category-1]
    categories_sorted[title] = None
    categories.pop(category-1)
    print(categories_sorted)



for email in emails.text:
    while True:
        print_screen(categories, email)
        selected = input("Select an action ")
        if selected == "1":
            print_screen(categories, email)
            category = int(input("Place in folder "))
            if (category <= len(categories)):
                categorize_email(email, selected)
                break; # Proceed to next email
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
