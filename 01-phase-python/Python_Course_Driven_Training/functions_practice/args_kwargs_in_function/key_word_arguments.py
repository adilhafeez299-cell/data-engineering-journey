# Keyword Arguments in Functions

# Example 1: Basic keyword arguments (no **kwargs)
#def get_posts_info(name, posts_qty):
    #info = f"{name} wrote {posts_qty} posts"
    #return info

#info = get_posts_info(name ='Bogdan', posts_qty=25)
#print(info)

# Order of the keyword arguments is not important when using keyword=value syntax
# The use of keyword arguments makes the code more readable

# Example 2: Using **kwargs to collect keyword arguments into a dictionary
def get_posts_info(**person):
    # **person collects all keyword arguments into a dictionary
    print(person)
    # {'name': 'Adil', 'posts_qty': 25}
    print(type(person)) # <class 'dict'>
    # Access dictionary values using keys
    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts"
    )
    return info

# Call function with keyword arguments - they become dict key-value pairs
info = get_posts_info(name ='Adil', posts_qty =25)
print(info)  # "Adil wrote 25 posts"