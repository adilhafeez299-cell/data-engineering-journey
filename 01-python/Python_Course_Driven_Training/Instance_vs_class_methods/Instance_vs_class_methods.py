class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1




first_comment = Comment("First comment")

print(first_comment.text)
print(first_comment.votes_qty)

first_comment.upvote()
print(first_comment.votes_qty)
