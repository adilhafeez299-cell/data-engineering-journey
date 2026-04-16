def image_info(data: dict):
    required_keys = ['image_id', 'image_title']

    for key in required_keys:
        if key not in data:
            raise TypeError(f"Missing required key: '{key}'")

    return f"Image '{data['image_title']}' has id {data['image_id']}"

img = {'image_id': 5136, 'image_title': 'my cat'}
try:
    result = image_info(img)
    print(result)
except TypeError as e:
    print(f"Error: {e}")
    #  go over this again, I need to understand it, perhaps go over Error handling again,
    # also may need to do a do-over for functions section
    