# User:
   # def info(self, username, email):
    #    print(f"User {username} has email {email}")

#first_user = User()
#first_user.username = 'Adil123'
#first_user.email = 'Adil.h1@kubernetes.com'
#first_user.info(**first_user.__dict__)


class User:
    def info(self):
        print(self.__dict__)
        print(f" {self.username} User has email {self.email}")

first_user = User()
first_user.username = 'bogdan123'
first_user.email = 'bog@bogman.com'

first_user.info()
