# Using Default Function Parameters - practical example

# Import date module for getting current date
from datetime import date

# Helper function to get the current weekday as a string
def get_weekday():
    # strftime('%A') formats the date to show the full weekday name
    return date.today().strftime('%A')

# Function that adds weekday information to a post dictionary
# weekday parameter has a default value from get_weekday() function call
def create_new_post(post, weekday=get_weekday()):
    # Create a shallow copy of the post dictionary to avoid modifying original
    post_copy = post.copy()
    # Add new key-value pair for the weekday
    post_copy['created_on_weekday'] = weekday
    return post_copy

# Create a simple post dictionary with id and author
initial_post = {
    'id': 243,
    'author': 'Bogdan',
}

# Call function without providing weekday argument
# It will use the default value from get_weekday()
post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)  # Shows original fields plus 'created_on_weekday'
#print(initial_post)  # Original post remains unchanged

