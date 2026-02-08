import re



def validate_email(email):
    email_regexp = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email_pattern = re.compile(email_regexp)
    is_valid = bool(email_pattern.match(email))
    return (email, is_valid)


print(validate_email('adil@gmail.com'))