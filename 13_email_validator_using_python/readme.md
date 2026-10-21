
# Introduction

Welcome to this course!

We will create a fully working **email validator program** using **Python**.

The program will ask for input from the user and will print output indicating whether the input is a valid email address or not.

Let's start coding!


# @ Symbol

## Introduction

Let's start by creating our function **`validate`**, which will decide whether an email address is valid or not.

When looking at an email address, the first thing that pops up is the **`@`** symbol. Every email address must include exactly one **`@`** symbol.

## Challenge

**Difficulty:** Easy

Write a function named **`validate`** that receives a string as input and returns `True` if the string contains exactly one **`@`** symbol; otherwise, it returns `False`.

## Solution

```python
def validate(email: str):
    return email.count('@') == 1
```

## Explanation of the Solution

### 1. Defining the Function

```python
def validate(email: str):
```

The function receives a string called `email`. The type hint `str` indicates that the input is expected to be a string.

### 2. Counting the `@` Symbol

```python
email.count('@')
```

The string method `count()` returns the number of times a specific character or substring appears in a string.

For example:

```python
email = "user@example.com"
print(email.count('@'))  # 1
```

### 3. Checking the Result

```python
return email.count('@') == 1
```

The comparison checks whether the `@` symbol appears exactly once.

- If it appears once, the function returns `True`.
- If it appears zero times or more than once, the function returns `False`.

## Examples

```python
print(validate("user@example.com"))  # True
print(validate("userexample.com"))   # False
print(validate("user@@example.com")) # False
```

Output:

```text
True
False
False
```

## Key Takeaway

The `count()` string method makes it easy to check how many times a character appears. By comparing the count with `1`, we ensure that the string contains exactly one `@` symbol.

**Note:** This is only the first validation rule. A string containing exactly one `@` symbol is not necessarily a valid email address; we will add more checks in the following steps.


# Recipient Name

## Introduction

**`john`**@gmail.com

The bold part is the **recipient name**.

The recipient name represents an email mailbox that belongs to:

- A specific person
- A mailing list
- A department
- A role within a company, such as sales or customer service

The recipient name may be a maximum of **64 characters** long and consist of:

- Uppercase and lowercase English letters (`A-Z`, `a-z`)
- Digits from `0` to `9`
- Special characters such as `! # $ % & ' * + - / = ? ^ _ \` { |`

A special character cannot appear as the first or last character in an email address or appear consecutively two or more times.

## Challenge

**Difficulty:** Medium

Add recipient name validation to the existing `validate` function.

For this validator, we will use simpler rules. The recipient name must be a **minimum of 3 characters** and a **maximum of 24 characters** long and consist of:

- Uppercase and lowercase English letters (`A-Z`, `a-z`)
- Digits from `0` to `9`
- The special characters `.` (dot) and `_` (underscore)

A special character cannot appear as the first or last character of the recipient name.

As before, the function **`validate`** should return `True` if the input email is valid according to the rules implemented so far, and `False` otherwise.

## Hint

### Hint 1

To check whether a character is allowed, create a variable like this:

```python
PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
```

To check whether a character `c` is included in `PERMITS`, use:

```python
c in PERMITS
```

## Solution

```python
PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'


def validate(email):
    if not email.count('@') == 1:
        return False

    recipient_name = email.split('@')[0]

    if len(recipient_name) > 24 or len(recipient_name) < 3:
        return False

    for c in recipient_name:
        if c not in PERMITS:
            return False

        if (
            '.' == recipient_name[0]
            or '.' == recipient_name[-1]
            or '_' == recipient_name[0]
            or '_' == recipient_name[-1]
        ):
            return False

    return True
```

## Explanation of the Solution

### 1. Defining the `PERMITS` Variable

```python
PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
```

The `PERMITS` variable contains all characters allowed in the recipient name:

- Lowercase English letters
- Uppercase English letters
- Digits
- Dots (`.`)
- Underscores (`_`)

This variable makes it easy to check whether each character is permitted.

### 2. Checking the `@` Symbol

```python
if not email.count('@') == 1:
    return False
```

The `count()` method counts how many times `@` appears in the email string.

If the count is not exactly `1`, the function immediately returns `False`.

### 3. Extracting the Recipient Name

```python
recipient_name = email.split('@')[0]
```

The `split('@')` method divides the email string wherever the `@` symbol appears.

Using `[0]` selects the part before `@`, which is the recipient name.

For example:

```python
email = "john_doe@gmail.com"
recipient_name = email.split('@')[0]

print(recipient_name)
```

Output:

```text
john_doe
```

### 4. Checking the Length

```python
if len(recipient_name) > 24 or len(recipient_name) < 3:
    return False
```

The `len()` function returns the number of characters in the recipient name.

The condition rejects names that:

- Contain more than 24 characters.
- Contain fewer than 3 characters.

Therefore, the recipient name must contain between **3 and 24 characters**, inclusive.

### 5. Checking Each Character

```python
for c in recipient_name:
    if c not in PERMITS:
        return False
```

The `for` loop examines each character in the recipient name.

The condition `c not in PERMITS` checks whether the current character is absent from the list of permitted characters.

If a character is not allowed, the function immediately returns `False`.

For example, a recipient name containing a space or `!` will fail this validation rule.

### 6. Checking the First and Last Characters

```python
if (
    '.' == recipient_name[0]
    or '.' == recipient_name[-1]
    or '_' == recipient_name[0]
    or '_' == recipient_name[-1]
):
    return False
```

This condition checks whether the recipient name starts or ends with a dot or underscore.

- `recipient_name[0]` accesses the first character.
- `recipient_name[-1]` accesses the last character.

If either character is `.` or `_`, the function returns `False`.

For example:

```python
print(validate(".john@gmail.com"))  # False
print(validate("john.@gmail.com"))  # False
print(validate("_john@gmail.com"))  # False
print(validate("john_@gmail.com"))  # False
```

### 7. Returning `True`

```python
return True
```

If the function passes all the validation checks, it returns `True`.

This means the email contains exactly one `@`, and its recipient name satisfies the length and character rules.

## Examples

```python
print(validate("john@gmail.com"))       # True
print(validate("john_doe@gmail.com"))   # True
print(validate("john.doe@gmail.com"))   # True

print(validate("jo@gmail.com"))         # False
print(validate(".john@gmail.com"))      # False
print(validate("john_@gmail.com"))      # False
print(validate("john!doe@gmail.com"))   # False
print(validate("john@@gmail.com"))      # False
```

## Key Takeaway

This challenge builds on the previous `@` validation by adding recipient name rules.

- `count('@')` ensures exactly one `@` symbol exists.
- `split('@')[0]` extracts the recipient name.
- `len()` checks the minimum and maximum length.
- `in` and `not in` check whether characters are allowed.
- Indexing with `[0]` and `[-1]` checks the first and last characters.

**Note:** This validator currently checks only the `@` symbol and recipient name. It does not yet validate the domain portion after `@`, so passing these checks does not guarantee that the entire email address is valid.

# Domain Name

## Introduction

For example, in the email address `john@**gmail**.com`, the bold part (`gmail`) is the domain name.

The domain name is a string of letters and digits that identifies a space on the Internet owned and controlled by a specific mailbox provider or organization.

Domain names may be a maximum of 253 characters and consist of:

- Uppercase and lowercase letters in English (A-Z, a-z)
- Digits from 0 to 9
- A hyphen (`-`)
- A period (`.`), used to identify a sub-domain. For example, `creator.coddy`.

## Challenge

**Difficulty:** Easy

Add support for **domain name validation** to the `validate` function.

In our validator, we will use simplified rules. The domain name must have a **minimum of 3 characters** and a **maximum of 12 characters**, and consist of:

- Uppercase and lowercase letters in English (A-Z, a-z)
- Digits from 0 to 9
- A hyphen (`-`)

As before, the `validate` function should return `True` if the input email is valid. Now, it must also validate the domain name.

> You don't need to support sub-domains. You can expect that no domain name containing a period (`.`) exists.

## Solution

```python
PERMITS_RECIPIENT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
PERMITS_DOMAIN = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'

def validate(email):
    if not email.count('@') == 1:
        return False

    recipient_name = email.split('@')[0]

    if len(recipient_name) > 24 or len(recipient_name) < 3:
        return False

    for c in recipient_name:
        if c not in PERMITS_RECIPIENT:
            return False

        if (
            '.' == recipient_name[0]
            or '.' == recipient_name[-1]
            or '_' == recipient_name[0]
            or '_' == recipient_name[-1]
        ):
            return False

    after_at = (email.split('@')[1])

    domain_name = after_at.split('.')[0]

    if len(domain_name) > 12 or len(domain_name) < 3:
        return False

    for c in domain_name:
        if c not in PERMITS_DOMAIN:
            return False

    return True
```

## Explanation

### 1. Define permitted characters

```python
PERMITS_RECIPIENT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
PERMITS_DOMAIN = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
```

- `PERMITS_RECIPIENT` contains all characters allowed in the recipient name: letters, digits, periods, and underscores.
- `PERMITS_DOMAIN` contains all characters allowed in the domain name: letters, digits, and hyphens.

The two strings are different because the recipient name and domain name have different character rules.

### 2. Check the `@` symbol

```python
if not email.count('@') == 1:
    return False
```

The email address must contain exactly one `@` symbol. If it contains none or more than one, the function returns `False`.

### 3. Extract and validate the recipient name

```python
recipient_name = email.split('@')[0]
```

The `split('@')` method separates the email address at the `@` symbol. Index `[0]` retrieves the part before it.

```python
if len(recipient_name) > 24 or len(recipient_name) < 3:
    return False
```

The recipient name must contain between 3 and 24 characters.

```python
for c in recipient_name:
    if c not in PERMITS_RECIPIENT:
        return False
```

The loop checks each character. If any character is not in `PERMITS_RECIPIENT`, the email address is rejected.

The following condition prevents the recipient name from starting or ending with a period or underscore:

```python
if (
    '.' == recipient_name[0]
    or '.' == recipient_name[-1]
    or '_' == recipient_name[0]
    or '_' == recipient_name[-1]
):
    return False
```

- `recipient_name[0]` accesses the first character.
- `recipient_name[-1]` accesses the last character.
- If either character is a period or underscore, the function returns `False`.

### 4. Extract the domain name

```python
after_at = (email.split('@')[1])

domain_name = after_at.split('.')[0]
```

- `email.split('@')[1]` retrieves everything after the `@` symbol.
- `after_at.split('.')[0]` retrieves the part before the first period.

For example, with `john@gmail.com`:

- `after_at` becomes `gmail.com`.
- `domain_name` becomes `gmail`.

This matches the challenge's simplified rule that sub-domains don't need to be supported.

### 5. Check the domain name length

```python
if len(domain_name) > 12 or len(domain_name) < 3:
    return False
```

The domain name must contain between 3 and 12 characters. If it is longer than 12 or shorter than 3, the function returns `False`.

### 6. Validate domain characters

```python
for c in domain_name:
    if c not in PERMITS_DOMAIN:
        return False
```

The loop checks every character in the domain name. Only English letters, digits, and hyphens are permitted.

If any character is not allowed, the function returns `False`.

### 7. Return `True`

```python
return True
```

If all the checks pass, the function returns `True`, meaning the email address satisfies the validation rules implemented here.

## Examples

| Email | Result | Reason |
|---|---|---|
| `john@gmail.com` | `True` | Valid recipient and domain |
| `johndoe@my-domain.com` | `True` | Domain contains a permitted hyphen |
| `john@ab.com` | `False` | Domain is shorter than 3 characters |
| `john@my_domain.com` | `False` | Underscore is not permitted in the domain |
| `john@my!domain.com` | `False` | Exclamation mark is not permitted in the domain |
| `@gmail.com` | `False` | Recipient name is empty |

## Key Takeaway

The main addition is **domain name validation**. By extracting the domain name, checking its length, and verifying each character against `PERMITS_DOMAIN`, the function now checks both the recipient name and the domain name.

The solution preserves the recipient-name limit of 3–24 characters from the previous challenge and applies the new 3–12 character limit to the domain name.

# Top-Level Domain

## Introduction

For example, in the email address `john@gmail.**com**`, the bold part (`com`) is the **top-level domain (TLD)**.

Top-level domains are the highest level of the domain name system for the Internet. They appear after the domain name in an email address.

Common top-level domains include:

- `com`
- `net`
- `org`

## Challenge

**Difficulty:** Easy

Add support for **top-level domain validation** to the `validate` function.

In our validator, we will use simplified rules. The top-level domain must be one of the following:

- `com`
- `net`
- `org`
- `tech`

Any other top-level domain should return `False`.

## Solution

```python
PERMITS_RECIPIENT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
PERMITS_DOMAIN = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
PERMITS_TOP = ['com', 'net', 'org', 'tech']

def validate(email):
    if not email.count('@') == 1:
        return False

    recipient_name = email.split('@')[0]

    if len(recipient_name) > 24 or len(recipient_name) < 3:
        return False

    for c in recipient_name:
        if c not in PERMITS_RECIPIENT:
            return False

        if (
            '.' == recipient_name[0]
            or '.' == recipient_name[-1]
            or '_' == recipient_name[0]
            or '_' == recipient_name[-1]
        ):
            return False

    after_at = (email.split('@')[1])

    domain_name = after_at.split('.')[0]

    if len(domain_name) > 12 or len(domain_name) < 3:
        return False

    for c in domain_name:
        if c not in PERMITS_DOMAIN:
            return False

    top_level_domain = after_at.split('.')[1]

    if top_level_domain not in PERMITS_TOP:
        return False

    return True
```

## Explanation

### 1. Define the permitted top-level domains

```python
PERMITS_TOP = ['com', 'net', 'org', 'tech']
```

This list contains the only top-level domains accepted by our validator. Any top-level domain not included in this list will cause the function to return `False`.

### 2. Extract the part after `@`

```python
after_at = (email.split('@')[1])
```

The `split('@')` method separates the email address at the `@` symbol. Index `[1]` retrieves everything after it.

For example, with `john@gmail.com`, `after_at` becomes `gmail.com`.

### 3. Extract the domain name

```python
domain_name = after_at.split('.')[0]
```

Splitting `gmail.com` at the period produces `['gmail', 'com']`. Index `[0]` retrieves `gmail`, which is the domain name.

The code then checks the domain's length and verifies that every character belongs to `PERMITS_DOMAIN`, as in the previous challenge.

### 4. Extract the top-level domain

```python
top_level_domain = after_at.split('.')[1]
```

Index `[1]` retrieves the part after the period.

For `john@gmail.com`, the top-level domain is `com`.

### 5. Check whether the top-level domain is permitted

```python
if top_level_domain not in PERMITS_TOP:
    return False
```

The `in` operator checks whether the top-level domain exists in the `PERMITS_TOP` list.

- If it is in the list, validation continues.
- If it is not in the list, the function returns `False`.

### 6. Return `True`

```python
return True
```

If all validation checks pass, the function returns `True`.

## Examples

| Email | Result | Reason |
|---|---|---|
| `john@gmail.com` | `True` | `com` is permitted |
| `john@gmail.net` | `True` | `net` is permitted |
| `john@gmail.org` | `True` | `org` is permitted |
| `john@gmail.tech` | `True` | `tech` is permitted |
| `john@gmail.info` | `False` | `info` is not in `PERMITS_TOP` |

## Key Takeaway

The main addition is **top-level domain validation**. By extracting the part after the period and checking it against `PERMITS_TOP`, the validator accepts only `com`, `net`, `org`, and `tech`.

This solution assumes the email address contains a period after the domain name, as specified by the simplified challenge rules.

# Call Validate

## Introduction

We finished the validation function!

Now let's call it all from the main function.

In Python, to create a main entry point, use:

```python
if __name__ == "__main__":
    # write code here
```

Write the code you want to execute inside the `if` clause.

The condition `if __name__ == "__main__":` checks whether the Python file is being run directly. If it is, the code inside the block will execute.

## Challenge

**Difficulty:** Easy

Create a main function entry point. Inside the `if __name__ == "__main__":` block:

1. Ask the user for input.
2. Use the `validate` function on the input.
3. Print the result returned by `validate`.

## Hint

To get input from the user, use:

```python
email = input()
```

Then call `validate` with `email` as the parameter.

## Solution

```python
PERMITS_RECIPIENT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
PERMITS_DOMAIN = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
PERMITS_TOP = ['com', 'net', 'org', 'tech']

def validate(email):
    if not email.count('@') == 1:
        return False

    recipient_name = email.split('@')[0]

    if len(recipient_name) > 24 or len(recipient_name) < 3:
        return False

    for c in recipient_name:
        if c not in PERMITS_RECIPIENT:
            return False

        if (
            '.' == recipient_name[0]
            or '.' == recipient_name[-1]
            or '_' == recipient_name[0]
            or '_' == recipient_name[-1]
        ):
            return False

    after_at = (email.split('@')[1])

    domain_name = after_at.split('.')[0]

    if len(domain_name) > 12 or len(domain_name) < 3:
        return False

    for c in domain_name:
        if c not in PERMITS_DOMAIN:
            return False

    top_level_domain = after_at.split('.')[1]

    if top_level_domain not in PERMITS_TOP:
        return False

    return True

if __name__ == "__main__":
    email = input()
    call = validate(email)
    print(call)
```

## Explanation

### 1. Check the main entry point

```python
if __name__ == "__main__":
```

Python sets the special variable `__name__` to `"__main__"` when the file is run directly.

This condition ensures that the code inside the block runs when the file is executed as the main program.

### 2. Get the user's input

```python
email = input()
```

The `input()` function waits for the user to enter an email address and press Enter. The entered text is stored in the `email` variable.

### 3. Call the validation function

```python
call = validate(email)
```

This passes the user's email address to `validate(email)`.

The function checks the recipient name, domain name, and top-level domain, then returns either `True` or `False`. That result is stored in the `call` variable.

### 4. Print the result

```python
print(call)
```

The `print()` function displays the result returned by `validate`.

- `True` means the email passed the implemented validation rules.
- `False` means the email failed at least one validation check.

## Example

**Input:**

```text
john@gmail.com
```

**Output:**

```text
True
```

Another example:

**Input:**

```text
john@gmail.info
```

**Output:**

```text
False
```

The second email fails because `info` is not included in `PERMITS_TOP`.

## Key Takeaway

The main entry point connects the validator to user input. The program reads an email, passes it to `validate()`, and prints the returned result.

```python
if __name__ == "__main__":
    email = input()
    call = validate(email)
    print(call)
```

This lets you run and test your completed email validator directly from the terminal.

# Last Additions

## Introduction

To wrap it all up, let's add clear messages to the user.

Instead of displaying `True` or `False`, our program will display a meaningful message indicating whether the email is valid or invalid. We'll also display a message asking the user to enter an email address before accepting input.

## Challenge

**Difficulty:** Easy

Add the following support to your program:

- Instead of printing `True` or `False`, print `"Email is valid"` or `"Email is invalid"`, depending on the result.
- Before asking the user for input, print the message `"Enter email:"` followed by a new line.

## Solution

```python id="v6px2q"
PERMITS_RECIPIENT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
PERMITS_DOMAIN = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
PERMITS_TOP = ['com', 'net', 'org', 'tech']

def validate(email):
    if not email.count('@') == 1:
        return "Email is invalid"

    recipient_name = email.split('@')[0]

    if len(recipient_name) > 24 or len(recipient_name) < 3:
        return "Email is invalid"

    for c in recipient_name:
        if c not in PERMITS_RECIPIENT:
            return "Email is invalid"

        if (
            '.' == recipient_name[0]
            or '.' == recipient_name[-1]
            or '_' == recipient_name[0]
            or '_' == recipient_name[-1]
        ):
            return "Email is invalid"

    after_at = (email.split('@')[1])

    domain_name = after_at.split('.')[0]

    if len(domain_name) > 12 or len(domain_name) < 3:
        return "Email is invalid"

    for c in domain_name:
        if c not in PERMITS_DOMAIN:
            return "Email is invalid"

    top_level_domain = after_at.split('.')[1]

    if top_level_domain not in PERMITS_TOP:
        return "Email is invalid"

    return 'Email is valid'

if __name__ == "__main__":
    email = input('Enter email:\n')
    call = validate(email)
    print(call)
```

## Explanation

### 1. Return meaningful messages from `validate`

Previously, the function returned Boolean values: `True` or `False`.

Now, each validation failure returns:

```python id="z3mn7b"
return "Email is invalid"
```

If the email passes all the validation checks, the function returns:

```python id="k3v8dp"
return 'Email is valid'
```

This makes the output easier for the user to understand.

### 2. Display the input prompt

```python id="w9d4qa"
email = input('Enter email:\n')
```

The `input()` function displays the prompt before waiting for the user's input.

- `'Enter email:'` is the message shown to the user.
- `\n` represents a newline, so the cursor moves to the next line before the user enters the email.
- The entered email is stored in the `email` variable.

### 3. Call the validation function

```python id="p2n6xc"
call = validate(email)
```

This passes the email address to `validate()` and stores the returned message in `call`.

### 4. Display the result

```python id="q5j8rm"
print(call)
```

The program prints the message returned by `validate()`.

## Example 1: Valid email

**Input:**

```text id="e8z4ka"
Enter email:
john@gmail.com
```

**Output:**

```text id="g5r2yc"
Email is valid
```

## Example 2: Invalid email

**Input:**

```text id="a3v9wn"
Enter email:
john@gmail.info
```

**Output:**

```text id="c7m4bx"
Email is invalid
```

The second email is rejected because `info` is not included in `PERMITS_TOP`.

## Key Takeaway

The final addition makes the program more user-friendly by displaying a clear input prompt and returning descriptive validation messages instead of Boolean values.

The program now follows this sequence:

1. Ask the user to enter an email address.
2. Validate the email.
3. Return a message indicating whether the email is valid.
4. Print that message to the terminal.

# Final Words

Well done!

You have created a fully working **email validator**!

But this is only the beginning. Here are some possible ways to improve your code:

- **Welcome message:** Display a welcome message when the program starts.
- **Repeated validation:** Repeatedly ask for input and validate email addresses, closing the program only when the user enters a specific command.
- **Better validation:** Improve the validation rules. In this project, we used simplified rules to keep things easier to understand.
- **Clean code:** Learn how to write cleaner, more readable, and maintainable code with [Learn at Coddy](https://coddy.tech/courses/clean_code__write_better_code_using_python)!

And there is so much more you can do!

**Happy Coding!** 🚀
