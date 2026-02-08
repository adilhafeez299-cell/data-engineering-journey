class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def info(self):
        print(f"User {self.username} has email {self.email}")




first_user = User('adil123','adil123@gmail.com')
first_user.info()
print(first_user.username)
print(first_user.email)
other_user = User('Jane123', 'Jane123@gmail.com')
other_user.info()
print(other_user.username)
print(other_user.email)

print(first_user.__dict__)

# next chapter is instance VS class methods
#go over this week starting 05/01/2025
