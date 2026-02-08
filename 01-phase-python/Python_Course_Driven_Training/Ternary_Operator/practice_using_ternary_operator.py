def convert_status_to_str(is_active):
    user_status_string = "Active" if is_active else "Inactive"
    return user_status_string

user_is_active = True

user_status = convert_status_to_str(user_is_active)
print(user_status)
