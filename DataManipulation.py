import time
def sq_for(x):
    for v in x:
        sq_x_for = []
        sq_x_for.append(v * v)
    return sq_x_for

def sq_comp(x):
    return [v * v for v in x]


