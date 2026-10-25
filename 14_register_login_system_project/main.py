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

    def login(self, username, password):
        # Check if the username exists in the system
        if username not in self.users:
            print("user isn't in the system")
        elif password != self.users[username]:
            print("password doesn't match")
        else:
            # Add the username to the logged-in users set
            self.logged_users.add(username)
            print("user logged in successfully")

    def sign_out(self, username):
        # Check if the username exists in the system
        if username not in self.users:
            print("user is not in the system")

        # Check if the user is currently logged in
        elif username not in self.logged_users:
            print("user is not logged in")

        else:
            # Remove the username from the logged-in users set
            self.logged_users.remove(username)
            print("user signed out successfully")
