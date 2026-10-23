class LoginSystem:
    def __init__(self):
        # Store registered users and their information as key-value pairs
        self.users = {}
        # Track currently logged-in users; a set prevents duplicates
        self.logged_users = set()
