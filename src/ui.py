import os

width = 80
height = 25
screen_bounds_x = 00
screen_bounds_y = 00
screen_bounds_x_max = width
screen_bounds_y_max = height
screenbuffer = screenbuffer = [[' ' for x in range(width)] for y in range(height)];


def draw():
    for row in screenbuffer:
        print(''.join(row))


def set_bounds(x=0, y=0, max_x=width, max_y=height): 
    global screen_bounds_x
    global screen_bounds_y
    global screen_bounds_x_max
    global screen_bounds_y_max
    screen_bounds_x = x
    screen_bounds_y = y
    screen_bounds_x_max = max_x
    screen_bounds_y_max = max_y


def draw_letter(x, y, letter):
    if (x >= screen_bounds_x_max or y >= screen_bounds_y_max):
        return;
    if (x < screen_bounds_x or y < screen_bounds_y):
        return
    screenbuffer[int(y)][int(x)] = letter


def clear():
    global width
    global height
    global screenbuffer
    size = os.get_terminal_size()
    width = size.columns-1
    height = size.lines-1
    screenbuffer = [[' ' for x in range(width)] for y in range(height)];
    set_bounds(0, 0, width, height)
    for x in range(width):
        for y in range(height):
            draw_letter(x, y, ' ')


def draw_string(x, y, wraplength, string):
    width = 0
    height = 0
    y_offset = 0
    for i in range(len(string)):
        x_cur = (i%wraplength)+x
        y_cur = (i-(i%wraplength))/wraplength+y+y_offset
        if string[i] == '\n':
            y_offset += 1
        else:
            draw_letter(int(x_cur), int(y_cur), string[i])
            if y_cur-y > height:
                height = y_cur-y
            if x_cur-x > width:
                width = x_cur-x

    return (width+1, height+1)

def draw_box(x, y, width, height):
    for x_offset in range(width):
        draw_letter(x+x_offset, y, '-')
        draw_letter(x+x_offset, y+height-1, '-')
    for y_offset in range(height):
        draw_letter(x, y+y_offset, '|')
        draw_letter(x+width-1, y+y_offset, '|')

    draw_letter(x, y, '+')
    draw_letter(x, y+height-1, '+')
    draw_letter(x+width-1, y, '+')
    draw_letter(x+width-1, y+height-1, '+')

def draw_categories(x, y, width, height, categories):
    i = 0

    start_x = x
    start_y = y

    set_bounds(start_x, start_y, start_x+width, start_y+height)
    draw_box(start_x, start_y, width, height)
    set_bounds(start_x+1, start_y+1, start_x+width-1, start_y+height-1)
    for category in categories:
        i += 1;
        (t_width, t_height) = draw_string(x+1, y+1, width-2, str(i)+" "+category)
        y += t_height;

    set_bounds()
