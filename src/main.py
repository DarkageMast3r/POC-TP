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

def categorize_email(email, category):
    print(email, category)


        



categories = ["Category 1", "Category 2", "abc", "def", "abcdefghijklmnopqrstuvwxyz"]

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
            categories.append(name)
        elif selected == "3":
            print_screen(categories, email)
            category = int(input("Remove category "))
            if (category <= len(categories)):
                categories.pop(int(category-1))


'''
print("Enter a line >")
for line in fileinput.input():
    print(line)
    vectors = vectorizer.transform(line)
    print(vectors)
    predicted = classifier.predict(vectors)
    print(predicted)
    print("Enter a line >")
'''

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
