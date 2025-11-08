#def get_posts_info(name, posts_qty):
    #info = f"{name} wrote {posts_qty} posts"
    #return info

#info = get_posts_info(name ='Bogdan', posts_qty=25)
#print(info)

# order of the keyword arguments is not important
# The use of keyword arguments makes the code more readable

# second example - more complex?
def get_posts_info(**person):
    print(person)
    # {'name': 'Adil', 'posts_qty': 25}
    print(type(person)) # <class, 'dict'>
    info = (
        f"{person['name']} wrote " 
        f"{person['posts_qty']} posts"
    )
    return info

info = get_posts_info(name ='Adil', posts_qty =25)
print(info)