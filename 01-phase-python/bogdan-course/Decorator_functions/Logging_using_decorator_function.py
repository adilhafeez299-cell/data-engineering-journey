def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling function {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        res = fn(*args, **kwargs)
        print(f"Result of the function is {res}")
        return res

    return wrapper

@log_function_call
def mult_number(a,b):
    return a*b

mult_number(2,3)

@log_function_call
def add_number(a,b):
    return a+b

add_number(2,3)
