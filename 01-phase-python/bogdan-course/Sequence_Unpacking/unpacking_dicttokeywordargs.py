def setup_database_connection(hostname, port, username, password):
    print(hostname, port, username, password)
    return {'hostname': hostname, 'port': port, 'username': username, 'password': password}

connection_data = {
    'hostname': 'localhost',
    'port': 3306,
    'username': 'root',
    'password': 'admin123'
}

data_base_setup = setup_database_connection(**connection_data)
print(data_base_setup)
