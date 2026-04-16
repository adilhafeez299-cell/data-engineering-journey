#Generate a CSRF token
import secrets
import string
print(secrets.token_hex(8))
print(secrets.token_hex(23))

print(secrets.token_urlsafe())
#https://mywebsite.com/reset-password?token=-PPq9qYlwQu2dBQYg1ve5kGzzWq0EIv6uYsHbCE530c
print(secrets.token_urlsafe(16))

def generate_otp_password(length):
    digits = string.digits
    password = ''.join(secrets.choice(digits) for _ in range (length))
    return password

print(generate_otp_password(10))
print(generate_otp_password(6))
print(generate_otp_password(3))
