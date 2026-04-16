class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author

class Forum:
    def __init__(self):
        self.users = []
        self.posts = []


    def register_user(self, username: str, email: str):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user

        return None

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user

        return None

    def find_posts_by_author(self, author: User):
        found_posts = []
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)
        return found_posts

# all logic should be encapsulated in the class

forum = Forum()

# user objects
admin = forum.register_user(username="admin", email="admin123@admin.com")
test_user = forum.register_user(username="test.user", email="adil@nmail.com")

print(forum.users)

forum.create_post("My first post", "Post content", admin)
forum.create_post("This is from test user", "Test Post Content", test_user)

#print(forum.posts[0].title)
#(forum.posts[0].content)
#print(forum.posts[0].author.username)
#print(forum.posts[0].author.email)

print(forum.find_user_by_username('ADMIN12345'))
print(forum.find_user_by_username('admin').username)
print(forum.find_user_by_username('test.user').email)

print(forum.find_user_by_email('admin123@admin.com').email)

forum.create_post("second great post", "this is the best post", admin)
found_posts = forum.find_posts_by_author(test_user)
found_posts_titles = [post.title for post in found_posts]
print(found_posts_titles)

found_posts_second_user = forum.find_posts_by_author(admin)
found_post_title = [post.title for post in found_posts_second_user]
print(found_post_title)

# Find user by email and find all posts by that user
user_email = 'admin123@admin.com'
found_user = forum.find_user_by_email(user_email)
if found_user:
    print(forum.find_posts_by_author(found_user))
else:
    print(f"User with email {user_email} doesn't exist")

