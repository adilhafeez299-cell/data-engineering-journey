def create_user(username, email, password):
    #creatiung user...
    return {'username': username, 'email': email, 'password': password}

user_details = {
    'username': 'ad_hafeez1',
    'email': 'adhafeez1@gmail.com',
    'password': 'admin123'
}

created_user = create_user(**user_details)
print(created_user)

user_other_details = ['alice-462', 'alice@alice.com', 'alice1232']
other_created_user = create_user(*user_other_details)
print(other_created_user)
