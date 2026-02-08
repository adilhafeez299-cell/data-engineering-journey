import secrets
import string

def generate_password(length: int):
    all_chars = string.ascii_letters + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_chars) for i in range(10))
    return password


print(generate_password(10))
print(generate_password(6))
print(generate_password(8))
# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)

