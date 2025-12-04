def image_info(image_data: dict) -> str:
    # Check if the keys exist in the dictionary you received
    if 'image_id' not in image_data or 'image_title' not in image_data:
        raise TypeError("Dictionary must contain 'image_id' and 'image_title'")

    # If we get here, both keys exist, so use them
    # ... your return statement

# Test case 1: Valid dictionary
my_image = {
    'image_id': 5136,
    'image_title': 'my cat'
}

try:
    result = image_info(my_image)  # Pass the dict to the function
    print(result)
except TypeError as e:
    print(f"Error: {e}")

# Test case 2: Missing a key
bad_image = {
    'image_id': 5136
    # Oops, forgot image_title!
}

try:
    result = image_info(bad_image)  # This should raise TypeError
    print(result)
except TypeError as e:
    print(f"Error: {e}")
