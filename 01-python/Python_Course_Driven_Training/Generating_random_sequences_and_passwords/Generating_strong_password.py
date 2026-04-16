import secrets
import string

# Counts how many times we try to generate password
counter = 0


def generate_password(length: int) -> str:
    global counter
    counter += 1

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    return password


def generate_special_password(length: int) -> str:
    while True:
        p = generate_password(length)

        if (
            any(c.islower() for c in p) and
            any(c.isupper() for c in p) and
            any(c.isdigit() for c in p) and
            any(c in string.punctuation for c in p)
        ):
            break

    return p


print(generate_special_password(3))
print(counter)



