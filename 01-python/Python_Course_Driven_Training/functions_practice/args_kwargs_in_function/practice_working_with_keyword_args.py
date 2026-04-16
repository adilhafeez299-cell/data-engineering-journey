# Practice - Working with keyword arguments vs positional arguments

# Example 1: Standard function with positional/keyword parameters
#def comments_info(comments_qty, day):
   # print(f'{comments_qty} comments were posted on {day}')

# Can call with keyword arguments in any order:
#comments_info(comments_qty = 50, day = 'monday')
#comments_info(day = 'tuesday', comments_qty = 43)
#comments_info(50, day = 'thursday')  # Mix positional and keyword

# Positional arguments matter when using them;
# To fix this we can use keyword arguments
# Can mix positional arguments with keyword arguments
# But if we were to swap this around we would get error
# Can NOT do comments_info(day = 'thursday', 50) - positional args must come before keyword args

# Example 2: Using *args to accept variable positional arguments
def comments_info(*args):
    # Access arguments by index since *args creates a tuple
    print(f'{args[0]} comments were posted on {args[1]}')

# Call with positional arguments only
comments_info(50, 'Monday')
# Single parameter with * in front means we can NOT use keyword arguments with this function
