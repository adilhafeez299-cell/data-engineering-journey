def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):
        print(args)
        print(kwargs)
        #some actions before execution of the original_fn function
        result = original_fn(*args, **kwargs)


        #some actions after execution of the original_fn function
        print("Executed after function")
        return result
    return wrapper_function


@decorator_function
def my_function(*args, **kwargs):
    print("This is my function")

my_function(10, name = 'Adil')
