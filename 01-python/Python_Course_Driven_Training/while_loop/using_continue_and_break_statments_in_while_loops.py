current_usernames = ['Adhafeez1','Sir_lacelot23', 'Elcucoye23']

while True:
    username = input("please enter desired username:")

    if username in current_usernames:
        print("username is already taken. please choose another")
        continue
    if len(username) < 5:
        print("username must be at least 5 characters long")
        continue
    current_usernames.append(username)
    break

print(f"welcome {username}")
input('type enter to continue')
print(f"this is you group {current_usernames}")
