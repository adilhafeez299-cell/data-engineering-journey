
def image_info(image_data: dict):
    if 'image_id' not in image_data or 'image_title' not in image_data:
        raise TypeError("Dictionary must contain 'image_id' and 'image_title'")

     # Build the string using values from dictionary
    result = f"image '{image_data['image_title']}' has id {image_data['image_id']}"
    return result

try:
    output = image_info({'image_id': 5136, 'image_title': 'my cat'})
    print(output)
except TypeError as e:
    print(f"Error: {e}")
