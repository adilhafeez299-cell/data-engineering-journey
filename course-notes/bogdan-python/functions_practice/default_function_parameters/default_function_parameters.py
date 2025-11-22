# Default Function Parameters - providing default values for parameters

# Example 1: Simple default parameter
#def mult_by_factor(value,  multiplier=1):
    # If multiplier is not provided, it defaults to 1
    #return value * multiplier

#print(mult_by_factor(10,2))  # multiplier=2, returns 20
#print(mult_by_factor(5))     # multiplier defaults to 1, returns 5

# Example 2: Using function call as default parameter value

# Import date module to get current date
from datetime import date

# Helper function that returns the current weekday name
def get_weekday():
    return date.today().strftime('%A')  # Returns day name like "Monday"

# Function with default parameter that calls get_weekday()
def create_new_post(post, weekday=get_weekday()):
    # Create a copy to avoid modifying the original dictionary
    post_copy = post.copy()
    # Add the weekday to the copied dictionary
    post_copy['created_on_weekday'] = weekday
    return post_copy

# Create initial post dictionary
initial_post = {
    'id': 243,
    'author': 'Bogdan',
}

# Call function without providing weekday - uses default (today's weekday)
post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)  # Shows post with 'created_on_weekday' added
#print(initial_post)  # Original post unchanged (we used .copy())