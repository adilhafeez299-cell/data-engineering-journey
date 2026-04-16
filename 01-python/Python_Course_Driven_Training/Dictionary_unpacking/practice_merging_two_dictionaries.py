default_settings = {'theme': 'light', 'font_size':16}
user_settings = {'font_size': 20, 'show_avatar': True}

merged_settings = {** default_settings, **user_settings}
print(merged_settings)
# value 16 was over_written
# order matters
# can merge more dictionaries if you want to

merged_settings = default_settings | user_settings
print(merged_settings)
# can use OR operator to merge dictionaries
