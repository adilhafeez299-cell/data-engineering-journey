#practice
# extending one class by another
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class AdminUser(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role
        self.isadmin = True

my_admin = AdminUser('admin123', 'admin@admin.com', 'Administrator')
print(my_admin.role)
print(type(my_admin))
print(isinstance(my_admin, AdminUser))
print(isinstance(my_admin, User))
print(isinstance(my_admin, object))

print(my_admin.__dict__)

my_user = User('user_test', 'user@user.com')
print(my_user.__dict__)
print(isinstance(my_user, User))
print(type(my_user))
