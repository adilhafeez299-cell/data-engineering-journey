def process_data(data):
    processed_data = data if data is not None else []

    return processed_data

received_data = [2, 4, 6, 8]
data = process_data(received_data)
print(data)