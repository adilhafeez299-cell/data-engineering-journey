def sum_fn(a, b):
    return a + b

def mult (a, b):
    return a*b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b
