class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1

    @staticmethod
    def format_post(title, content):
        return (
            f"Post title: {title}\n"
            f"Post content: {content}"
        )

formatted_post = Post.format_post("Some post title", "Post contents")
print(formatted_post)