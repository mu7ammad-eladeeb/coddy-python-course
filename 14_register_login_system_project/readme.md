# Introduction

Welcome to this project!

Here, you will have the opportunity to see how a simple **user management system** is structured and handled in Python.

You will learn:

- What a **`set`** is and what its use cases are.
- How to register, sign out, and log in users to your system.
- A basic cryptography demonstration to encrypt and decrypt passwords.

Sounds interesting? Let's go! 🚀

# How to Use a Set

A **`set`** in Python is a collection that manages data similarly to dictionary keys, but without values.

## Creating a Set

To create an empty set, use:

```python
new_set = set()
```

A set can contain only one occurrence of each element. Duplicate elements are automatically ignored.

## Adding Elements to a Set

For example, let's add an element to our `new_set`:

```python
new_set.add(1)
print(new_set)
>>> {1}
```

As of now, we have only one element: the integer **`1`**.

If we try to add another integer `1` to the set:

```python
new_set.add(1)
```

It won't affect `new_set` because it already contains this element.

After printing `new_set` again:

```python
print(new_set)
>>> {1}
```

We get the same result because sets do not store duplicate elements.

## Removing Elements from a Set

To delete an item from a set, use **`.remove(element)`**:

```python
new_set.remove(1)
print(new_set)
>>> set()
```

The set is now empty because we removed its only element.

## Checking Whether an Element Exists

Another important feature is the ability to check whether an item is already in our set:

```python
if 1 in new_set:
    print("1 integer is in our new_set")
elif "1" in new_set:
    print("1 string is in our new_set")
else:
    print("no 1 is in our new_set")
>>> "1 integer is in our new_set"
```

**Note:** This output assumes `new_set` contains the integer `1` when the code runs. If the set is still empty after the previous removal, the output will be `"no 1 is in our new_set"`.

The integer `1` and the string `"1"` are different elements because they have different types.

## Challenge

**Difficulty:** Easy

Create a function named **`maintain_set`** that receives a set of integers and an integer.

The function should:

- Check whether the integer is in the set.
- If it is, return that integer multiplied by `2`.
- If it is not, insert it into the set and return the set.

## Solution

```python
def maintain_set(a_set, number):
    if number in a_set:
        return number * 2

    a_set.add(number)
    return a_set
```

## Explanation

### 1. Define the function

```python
def maintain_set(a_set, number):
```

The function receives two arguments:

- `a_set`: the set of integers.
- `number`: the integer we want to check.

### 2. Check whether the integer exists

```python
if number in a_set:
    return number * 2
```

The `in` operator checks whether `number` is already an element of `a_set`.

If the integer exists, the function returns it multiplied by `2`.

For example, if `number` is `3` and `3` is already in the set, the function returns `6`.

### 3. Add the integer if it doesn't exist

```python
a_set.add(number)
return a_set
```

If the integer is not in the set, `.add(number)` inserts it into `a_set`.

The function then returns the updated set.

## Examples

```python
my_set = {1, 2, 3}

print(maintain_set(my_set, 2))
>>> 4

print(maintain_set(my_set, 5))
>>> {1, 2, 3, 5}
```

In the first example, `2` already exists in the set, so the function returns `4`.

In the second example, `5` does not exist in the set, so it is added and the updated set is returned.

## Key Takeaway

Sets are useful when you need to store unique elements and check whether an element exists.

- **`.add(element)`** inserts an element into a set.
- **`element in a_set`** checks whether an element exists in a set.
- **`return number * 2`** returns the doubled number when it is already present.

The function uses these features to decide whether to return a calculated value or an updated set.

# Initializing

A user management system requires us to keep track of registered users and logged-in users.

To do this, we need two data structures:

- A **dictionary** to store registered users and their information.
- A **set** to keep track of users who are currently logged in.

## Challenge

**Difficulty:** Easy

Create a class named **`LoginSystem`** that doesn't receive anything in its constructor other than `self`.

Inside `__init__(self)`, initialize the following variables:

- `users` as an empty dictionary.
- `logged_users` as an empty set.

## Hints

### Hint 1: Create an empty dictionary

To create an empty dictionary, use:

```python
variable = {}
```

A dictionary stores data as key-value pairs. In our login system, it will be used to keep track of registered users.

### Hint 2: Create an empty set

To create an empty set, use:

```python
variable = set()
```

A set stores unique elements. In our login system, it will be used to track logged-in users without storing duplicates.

## Solution

```python
class LoginSystem:
    def __init__(self):
        self.users = {}
        self.logged_users = set()
```

## Explanation

### 1. Define the class

```python
class LoginSystem:
```

This creates a class named `LoginSystem`, which will manage registered users and logged-in users.

### 2. Define the constructor

```python
def __init__(self):
```

The `__init__` method is the constructor. Python calls it automatically when a new instance of the class is created.

The `self` parameter refers to the current instance of the class.

### 3. Initialize the registered users

```python
self.users = {}
```

This creates an empty dictionary named `users`.

We use `self.users` so the dictionary belongs to the instance and can be accessed by other methods in the class.

### 4. Initialize the logged-in users

```python
self.logged_users = set()
```

This creates an empty set named `logged_users`.

A set is useful here because each user should appear only once in the collection of logged-in users.

## Example

```python
system = LoginSystem()

print(system.users)
>>> {}

print(system.logged_users)
>>> set()
```

When we create a `LoginSystem` object, both data structures are initialized and ready to use.

## Key Takeaway

The `LoginSystem` class uses two different data structures for two different purposes:

- `self.users = {}` stores registered users in a dictionary.
- `self.logged_users = set()` tracks users who are currently logged in.

This initializes the foundation of our user management system.

# Register

## Challenge

**Difficulty:** Easy

To allow users to register, create a method **`register(self, username, password)`** that receives a username and password.

All registered users will be stored inside the **`users`** variable that we initialized in the previous lesson. The keys are the usernames, and the values are the passwords.

The method should check whether a user is already registered in the system:

- If the user is **not registered**, add the username and password to `self.users` and print `user registered successfully`.
- If the user **is already registered**, print `user already exists`.

## Hints

**Hint 1:** To keep track of registered users, use the **`self.users`** variable.

**Hint 2:** To check if a user is already in the system, use:

```python
if username in self.users:
```

## Solution

```python
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
```

## Explanation

1. **Check whether the username exists:**  
   `if username in self.users:` checks whether the username is already a key in the `users` dictionary.

2. **Handle an existing user:**  
   If the username is already in the dictionary, print `user already exists`. This prevents the same username from being registered twice.

3. **Register a new user:**  
   If the username is not in the dictionary, `self.users[username] = password` adds the username as the key and the password as its value.

4. **Confirm successful registration:**  
   Print `user registered successfully` to let the user know the registration worked.

## Example

```python
system = LoginSystem()

system.register("alice", "pass123")
# Output: user registered successfully

system.register("alice", "anotherpass")
# Output: user already exists

print(system.users)
# Output: {'alice': 'pass123'}
```

**Key takeaway:** Use a dictionary (`self.users`) to store registered users, check whether a username already exists before adding it, and print the appropriate message for each outcome.

# Login

## Challenge

**Difficulty:** Easy

Now that we can register users, it is time to create a method for logging them in.

Create a method called `login(self, username, password)` that checks whether the user exists in the system. If the user exists, check whether the provided password matches the password stored in the system. If both conditions are met, store the username in the `logged_users` variable.

The method should display the following messages:

- If the user logs in successfully, print `user logged in successfully`.
- If the user is not registered in the system, print `user isn't in the system`.
- If the password doesn't match, print `password doesn't match`.

## Hints

**Hint 1:** To check if the user exists in the system, use:

```python
if username in self.users:
```

**Hint 2:** To add a user to the set, use:

```python
self.logged_users.add(username)
```

## Solution

```python
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
```

## Explanation

1. **Check whether the user exists**

   `if username in self.users:` checks whether the username is a key in the `users` dictionary.

2. **Check the password**

   `self.users[username] == password` compares the provided password with the password stored for that username.

3. **Add the user to `logged_users`**

   If the username exists and the password matches, `self.logged_users.add(username)` adds the username to the set of logged-in users.

   A set stores unique values, so the same username won't be added more than once.

4. **Print the appropriate message**

   The method prints a different message depending on whether the username is missing, the password is incorrect, or the login succeeds.

## Example

```python
system = LoginSystem()

system.register("alice", "pass123")
# Output: user registered successfully

system.login("alice", "pass123")
# Output: user logged in successfully

system.login("alice", "wrongpass")
# Output: password doesn't match

system.login("bob", "pass123")
# Output: user isn't in the system

print(system.logged_users)
# Output: {'alice'}
```

## Key Takeaway

The `users` dictionary stores registered usernames and passwords, while the `logged_users` set tracks users who have successfully logged in.

**Important:** This example stores passwords as plain text for learning purposes. Real applications should store securely hashed passwords instead of plain-text passwords.
