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

Now, we have only one element: the integer **`1`**.

If we try to add another integer `1` to the set:

```python
new_set.add(1)
```

It won't affect `new_set` because the element already exists.

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

Another important feature is the ability to check whether an item is already in our set.

```python
if 1 in new_set:
    print("1 integer is in our new_set")
elif "1" in new_set:
    print("1 string is in our new_set")
else:
    print("no 1 is in our new_set")
>>> "1 integer is in our new_set"
```

**Note:** The result above assumes that `new_set` contains the integer `1` when this code runs. If the set is still empty after the previous removal, the output will instead be `"no 1 is in our new_set"`.

Notice that the integer `1` and the string `"1"` are different elements. A set can contain both because they have different types.

## Challenge

**Difficulty:** Easy

Create a function named **`maintain_set`** that receives a set of integers and an integer.

The function should:

- Check whether the integer is already in the set.
- If it is in the set, return that integer multiplied by `2`.
- If it is not in the set, insert it into the set and return the set.

## Solution

```python
def maintain_set(numbers, number):
    if number in numbers:
        return number * 2

    numbers.add(number)
    return numbers
```

## Explanation

### 1. Define the function

```python
def maintain_set(numbers, number):
```

The function receives two arguments:

- `numbers`: the set of integers.
- `number`: the integer we want to check.

### 2. Check whether the integer exists

```python
if number in numbers:
    return number * 2
```

The `in` operator checks whether `number` is already an element of `numbers`.

If it exists, the function returns the integer multiplied by `2`.

### 3. Add the integer if it doesn't exist

```python
numbers.add(number)
return numbers
```

If the integer is not in the set, `.add(number)` inserts it. The function then returns the updated set.

## Examples

```python
my_set = {1, 2, 3}

print(maintain_set(my_set, 2))
>>> 4

print(maintain_set(my_set, 5))
>>> {1, 2, 3, 5}
```

In the first example, `2` is already in the set, so the function returns `4`.

In the second example, `5` is not in the set, so it is added and the updated set is returned.

**Key takeaway:** Sets are useful when you need to store unique elements and quickly check whether an element exists. The `.add()` method inserts an element, while the `in` operator checks for membership.
