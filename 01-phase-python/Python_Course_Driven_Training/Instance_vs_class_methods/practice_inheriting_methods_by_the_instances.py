class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1


my_post = Post("My first post", "This is my first post", "Bogdan")

print(my_post)
print(my_post.title)
print(my_post.likes_qty)

my_post.like()
my_post.like()
print(my_post.likes_qty)


Post.like(my_post)
print(my_post.likes_qty)
