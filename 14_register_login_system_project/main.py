class LoginSystem:
    def __init__(self):
        # Store registered users as username-password pairs
        self.users = {}

        # Track currently logged-in users
        self.logged_users = set()

    def register(self, username, password):
        # Check if the username is already registered
        if username in self.users:
            print("user already exists")
        else:
            # Store the username as the key and password as the value
            self.users[username] = password
            print("user registered successfully")
