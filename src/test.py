inputs = []
i = 0

def read():
    global i
    if i >= len(inputs):
        return (false, None)
    val = inputs[i]
    i += 1
    return (true, val)

def write(val):
    global inputs
    inputs = inputs + val

def create_category(name):
    return
