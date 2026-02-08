# practice working with class attributes



class User:
    users_qty = 0
    # this is class attribute, counts total users registered in the system


    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.users_qty += 1

first_user =  User('bob234', 'bob@bob.com')
second_user = User('Alice', 'Alice@alice234.com')
third_user =  User('john324', 'john@shoenice.com')

print(User.users_qty)