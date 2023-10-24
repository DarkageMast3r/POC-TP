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

emails = pd.read_csv("emails.csv")

screen_width = 80
screen_height = 25
screen_bounds_x = 00
screen_bounds_y = 00
screen_bounds_x_max = screen_width
screen_bounds_y_max = screen_height
screenbuffer = screenbuffer = [[' ' for x in range(screen_width)] for y in range(screen_height)];


def screenbuffer_print():
    for row in screenbuffer:
        print(''.join(row))


def screenbuffer_set_bounds(x=0, y=0, max_x=screen_width, max_y=screen_height): 
    global screen_bounds_x
    global screen_bounds_y
    global screen_bounds_x_max
    global screen_bounds_y_max
    screen_bounds_x = x
    screen_bounds_y = y
    screen_bounds_x_max = max_x
    screen_bounds_y_max = max_y



def screenbuffer_draw_letter(x, y, letter):
    if (x >= screen_bounds_x_max or y >= screen_bounds_y_max):
        return;
    if (x < screen_bounds_x or y < screen_bounds_y):
        return
    screenbuffer[int(y)][int(x)] = letter


def screenbuffer_clear():
    screenbuffer = [[' ' for x in range(screen_width)] for y in range(screen_height)];
    screenbuffer_set_bounds()
    for x in range(screen_width):
        for y in range(screen_height):
            screenbuffer_draw_letter(x, y, ' ')

def screenbuffer_draw_string(x, y, wraplength, string):
    width = 0
    height = 0
    y_offset = 0
    for i in range(len(string)):
        x_cur = (i%wraplength)+x
        y_cur = (i-(i%wraplength))/wraplength+y+y_offset
        if string[i] == '\n':
            y_offset += 1
        else:
            screenbuffer_draw_letter(int(x_cur), int(y_cur), string[i])
            if y_cur-y > height:
                height = y_cur-y
            if x_cur-x > width:
                width = x_cur-x

    return (width+1, height+1)



def print_box(x, y, width, height):
    for x_offset in range(width):
        screenbuffer_draw_letter(x+x_offset, y, '-')
        screenbuffer_draw_letter(x+x_offset, y+height-1, '-')
    for y_offset in range(height):
        screenbuffer_draw_letter(x, y+y_offset, '|')
        screenbuffer_draw_letter(x+width-1, y+y_offset, '|')

    screenbuffer_draw_letter(x, y, '+')
    screenbuffer_draw_letter(x, y+height-1, '+')
    screenbuffer_draw_letter(x+width-1, y, '+')
    screenbuffer_draw_letter(x+width-1, y+height-1, '+')

def print_categories(x, y, width, height, categories):
    i = 0

    start_x = x
    start_y = y
    print_box(start_x, start_y, width, height)
    screenbuffer_set_bounds(start_x+1, start_y+1, start_x+width-1, start_y+height-1)
    for category in categories:
        i += 1;
        (t_width, t_height) = screenbuffer_draw_string(x+1, y+1, width-2, str(i)+" "+category)
        y += t_height;

    screenbuffer_set_bounds()


def print_screen(categories, email):
    screenbuffer_clear()
    print_categories(0, 0, 15, 15, categories)

    screenbuffer_set_bounds(15, 0, 80, 26)
    screenbuffer_draw_string(16, 1, 63, email)
    print_box(15, 0, 65, 25)

    screenbuffer_set_bounds()
    print_categories(0, 15, 15, 10, ["Categorize", "New category", "Delete category"]);
    screenbuffer_set_bounds()

    screenbuffer_print()


def categorize_email(email, category):
    print(email, category)


        



categories = ["Category 1", "Category 2", "abc", "def", "abcdefghijklmnopqrstuvwxyz"]

for email in emails.text:
    while True:
        print_screen(categories, email)
        selected = int(input("Select an action:"))
        if selected == 1:
            category = int(input("Select a category:"))
            if (category <= len(categories)):
                categorize_email(email, selected)
                break; # Proceed to next email
        elif selected == 2:
            name = (input("Select a name:"))
            categories.append(name)
        elif selected == 3:
            category = int(input("Select a category:"))
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
