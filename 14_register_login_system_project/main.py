class LoginSystem:
    def __init__(self):
        # Store registered users as username-password pairs
        self.users = {}

        # Store usernames of users who are currently logged in
        self.logged_users = set()

    def register(self, username, password):
        # Check if the username is already registered
        if username in self.users:
            print("user already exists")
        else:
            # Store the username and password
            self.users[username] = password
            print("user registered successfully")

    def login(self, username, password):
        # Check if the username exists in the system
        if username in self.users:
            # Check if the provided password matches the stored password
            if self.users[username] == password:
                # Add the username to the set of logged-in users
                self.logged_users.add(username)
                print("user logged in successfully")
            else:
                # The password is incorrect
                print("password doesn't match")
        else:
            # The username is not registered
            print("user isn't in the system")
