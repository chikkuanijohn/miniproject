users = {}

def register_user(username, password):
    if username in users:
        return "User already exists!"
    users[username] = {'password': password, 'bookings': []}
    return "User registered successfully!"

def login_user(username, password):
    if username in users and users[username]['password'] == password:
        return "Login successful!"
    return "Invalid username or password!"