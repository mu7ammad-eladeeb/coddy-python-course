class LoginSystem:
    def __init__(self):
        # Store registered usernames and encrypted passwords
        self.users = {}

        # Track currently logged-in users
        self.logged_users = set()

        # Map each letter to its encrypted equivalent
        self.mapping = {
            "a": "i", "b": "l", "c": "q", "d": "f", "e": "z", "f": "s",
            "g": "a", "h": "g", "i": "e", "j": "p", "k": "w", "l": "o",
            "m": "v", "n": "u", "o": "b", "p": "j", "q": "k", "r": "n",
            "s": "x", "t": "d", "u": "h", "v": "y", "w": "t", "x": "m",
            "y": "r", "z": "c"
        }

    def encrypt(self, password):
        # Store the encrypted characters
        new_values = []

        # Replace each character using the mapping
        for char in password:
            if char in self.mapping:
                new_values.append(self.mapping[char])
            else:
                # Keep characters that are not in the mapping unchanged
                new_values.append(char)

        # Combine the characters into one string
        return "".join(new_values)

    def register(self, username, password):
        # Check if the username is already registered
        if username in self.users:
            print("user already exists")
        else:
            # Encrypt the password before storing it
            self.users[username] = self.encrypt(password)
            print("user registered successfully")

    def login(self, username, password):
        # Check if the username exists
        if username not in self.users:
            print("user isn't in the system")
        # Encrypt the input and compare it with the stored password
        elif self.encrypt(password) != self.users[username]:
            print("password doesn't match")
        else:
            # Add the username to the logged-in users set
            self.logged_users.add(username)
            print("user logged in successfully")

    def sign_out(self, username):
        # Check if the username exists
        if username not in self.users:
            print("user is not in the system")
        # Check if the user is logged in
        elif username not in self.logged_users:
            print("user is not logged in")
        else:
            # Remove the username from the logged-in users set
            self.logged_users.remove(username)
            print("user signed out successfully")
