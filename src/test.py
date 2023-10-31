inputs = []
i = 0

def read():
    global i
    if i >= len(inputs):
        return (False, None)
    val = inputs[i]
    i += 1
    return (True, val)

def write(val):
    inputs.append(val)

def create_category(name):
    write("2")
    write(name)

def categorize(folder, doLearn):
    if doLearn:
        write("1")
    else:
        write("4")
    write(str(folder))

def expect(folder):
    write("7")
    write(str(folder))

def reset():
    write("6")

def report_results():
    write("8")

def skip():
    write("5")
