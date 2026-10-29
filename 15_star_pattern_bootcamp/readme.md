# Introduction

Star patterns are an excellent way for beginners to master the fundamentals of programming logic, loops, and conditional statements.

This course provides a hands-on approach to learning programming by coding a diverse range of star patterns, from simple to complex designs. Through these engaging exercises, you will develop problem-solving skills, enhance your understanding of control structures, and gain confidence in writing clean and efficient code.

Solving problems is a great way to improve your thinking skills and become more familiar with the programming language you're learning.

In this series of challenges about **Patterns**, you will find tasks that enhance your problem-solving abilities and push you to think critically about solutions.

**Happy Coding!**

# Instructions to Follow

**Follow the instructions below to get the desired output pattern:**

1. Get a clear understanding of the **expected output pattern** provided.
2. Implement your own logic in your preferred language to print the pattern. You can choose a different approach from the provided hints or solution.
3. When comparing your output with the expected output, make sure to focus on the empty space **`"* _"`** after the star to obtain the desired result.
4. Pick the language you prefer. There are no restrictions on how you can solve the challenge, so explore various methods and find the one that suits you best.
5. Everything is in order!

To succeed in this course, it is important to **actively engage with the material**. Be sure to attempt the challenges on your own first. If you encounter difficulty, you can refer to the hints and eventually the solution, if necessary.

> **Note:** This course is not for total beginners. You will need a good understanding of your preferred programming language. If you are a beginner, please check out topics related to conditional statements, nested loops, and functions in your preferred language.

# Row of Stars

## Challenge

**Difficulty:** Easy

Your first challenge is to create a simple yet iconic pattern using asterisks (`*`).

Your task is to write a program that prints a **single row** of stars. The pattern consists of **1 row and 6 columns**.

### Expected Output Pattern

```text
* * * * * *
```

## Hints

1. Use a `for` loop to repeat a print action.
2. Use the `end` argument with a space (`" "`) to separate the stars.

## Solution

```python
for i in range(6):
    print("*", end=" ")
```

## Explanation

1. **`for i in range(6):`** repeats the loop 6 times because `range(6)` generates six values, from `0` to `5`.
2. **`print("*", end=" ")`** prints one star followed by a space instead of moving to a new line.
3. After all six iterations, the stars appear on a single row, separated by spaces.

### Key Takeaway

The `for` loop controls how many stars are printed, while `end=" "` keeps them on the same line and separates them with spaces.

# Column of Stars

## Challenge

**Difficulty:** Easy

Your task is to write a program that prints a **single column** of stars. The pattern consists of **6 rows and 1 column**.

### Expected Output Pattern

```text
*
*
*
*
*
*
```

## Hint

Use a `for` loop to repeat a print action.

## Solution

```python
for i in range(6):
    print("*")
```

## Explanation

1. **`for i in range(6):`** repeats the loop 6 times. The variable `i` takes values from `0` to `5`.
2. **`print("*")`** prints one star during each iteration.
3. By default, `print()` ends with a newline (`"\n"`), so each star appears on a separate line.

## Key Takeaway

Unlike the row-of-stars challenge, you don't need `end=" "` here. The default behavior of `print()` automatically moves to a new line after each star.

# Solid Square of Stars

## Challenge

**Difficulty:** Easy

Your task is to write a program that prints a **solid square** of stars. The pattern consists of **6 rows and 6 columns**.

### Expected Output Pattern

```text
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
```

## Hints

1. Use **nested loops**—one for rows and one for columns—to control where stars are placed.
2. Inside the inner loop, print a star followed by a space (`"* "`).
3. Use `print()` without arguments after the inner loop to move to the next line for each row.
4. Adjust `range(6)` to control the number of stars printed horizontally and vertically.

## Solution

```python
for row in range(6):
    for col in range(6):
        print("*", end=" ")
    print()
```

## Explanation

### 1. The outer loop controls the rows

```python
for row in range(6):
```

The outer loop runs 6 times, creating the **6 rows** of the square.

### 2. The inner loop controls the columns

```python
for col in range(6):
    print("*", end=" ")
```

For each row, the inner loop runs 6 times, printing 6 stars.

The argument `end=" "` adds a space after each star instead of moving to a new line. This keeps all 6 stars on the same row.

### 3. Move to the next row

```python
print()
```

After the inner loop finishes, `print()` moves the output to a new line so the next iteration of the outer loop can print the next row.

## How the Nested Loops Work

- The outer loop runs **6 times**.
- For every iteration of the outer loop, the inner loop runs **6 times**.
- Each inner-loop iteration prints one star.
- After each row is complete, `print()` moves to the next line.

The total number of stars printed is:

\[
6 \times 6 = 36
\]

## Key Takeaway

**Nested loops** are useful for printing patterns with rows and columns. The outer loop controls the number of rows, while the inner loop controls the number of stars in each row.

# Right-Angle Triangle

## Challenge

**Difficulty:** Easy

Write a program that prints a **right-angle triangle** of stars as shown below. The pattern consists of **6 rows and 6 columns**.

### Expected Output Pattern

```text
*
* *
* * *
* * * *
* * * * *
* * * * * *
```

## Hints

1. Use `range(1, rows + 1)` to iterate from `1` to `rows` (inclusive).
2. Use `"* " * i` to print `i` stars followed by spaces.
3. Each row increases the number of stars printed by 1, creating a right-angle triangle pattern.

## Solution

```python
rows = 6

for i in range(1, rows + 1):
    print("* " * i)
```

## Explanation

1. **`rows = 6`** sets the number of rows in the triangle.
2. **`range(1, rows + 1)`** generates the numbers from `1` to `6`. The upper limit is exclusive, so we use `rows + 1` to include `6`.
3. **`"* " * i`** repeats the string `"* "` exactly `i` times.
4. **`print()`** prints the repeated stars and moves to the next line.

## How the Pattern Is Created

| Iteration (`i`) | Expression | Stars printed |
|---:|---|---|
| 1 | `"* " * 1` | `*` |
| 2 | `"* " * 2` | `* *` |
| 3 | `"* " * 3` | `* * *` |
| 4 | `"* " * 4` | `* * * *` |
| 5 | `"* " * 5` | `* * * * *` |
| 6 | `"* " * 6` | `* * * * * *` |

## Key Takeaway

You can create a growing star pattern using a single loop and string repetition. The loop variable `i` determines how many stars appear on each row, increasing from one star to six.

# Left-Angle Triangle

## Challenge

**Difficulty:** Easy

Write a program that prints a **left-angle triangle** of stars as shown below. The pattern consists of **6 rows and 6 columns**.

### Output Pattern

```text
          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
```

## Hints

1. Use the first loop to iterate through rows and the second loop for leading whitespaces.
2. The loop `for j in range(2 * (rows - i) - 1)` prints leading whitespaces to align stars properly.
3. The loop `for k in range(i + 1)` prints the star (`"* "`) characters.
4. Use `print()` after the inner loops to move to the next line for each row.

## Solution 1: Using Nested Loops

```python
rows = 6

for i in range(rows):
    for j in range(2 * (rows - i) - 1):
        print(" ", end="")

    for k in range(i + 1):
        print("* ", end="")

    print()
```

### Explanation

1. **`rows = 6`** sets the number of rows in the triangle.
2. **`for i in range(rows)`** runs six times, with `i` going from `0` to `5`.
3. **`for j in range(2 * (rows - i) - 1)`** prints leading spaces before the stars. The number of spaces decreases as the rows progress.
4. **`for k in range(i + 1)`** prints the stars. Each new row contains one more star than the previous row.
5. **`print("* ", end="")`** prints each star on the same line because `end=""` prevents `print()` from moving to a new line.
6. **`print()`** moves to the next line after the spaces and stars for the current row have been printed.

### How the Pattern Is Created

| Row (`i`) | Leading spaces | Number of stars |
|---:|---:|---:|
| 0 | 11 | 1 |
| 1 | 9 | 2 |
| 2 | 7 | 3 |
| 3 | 5 | 4 |
| 4 | 3 | 5 |
| 5 | 1 | 6 |

The leading spaces decrease by two on each row, while the number of stars increases by one.

## Solution 2: Using String Repetition and Slicing

```python
# Write code here
stars = "*"
spaces = "           "

for i in range(6):
    print(spaces + stars)
    stars += " *"
    spaces = spaces[:-2]
```

### Explanation

1. **`stars = "*"`** initializes the pattern with one star.
2. **`spaces = "           "`** creates a string containing 11 spaces to position the first star on the right.
3. **`for i in range(6)`** repeats the process six times, creating six rows.
4. **`print(spaces + stars)`** combines the leading spaces and the current star pattern, then prints them on one line.
5. **`stars += " *"`** adds another star, preceded by a space, for the next row.
6. **`spaces = spaces[:-2]`** removes the last two spaces from the leading-spaces string. This shifts the next row's stars two positions to the left.

### How String Slicing Works

The expression `spaces[:-2]` creates a new string containing everything except the last two characters.

For example:

```python
spaces = "     "
spaces = spaces[:-2]

print(repr(spaces))
```

Output:

```text
'   '
```

The string now contains three spaces instead of five.

## Key Takeaway

Both solutions produce the same left-angle triangle, but they use different approaches:

- **Solution 1** uses nested loops to control the number of leading spaces and stars on each row.
- **Solution 2** builds the pattern by adding stars and shortening the spaces string on every iteration.

The nested-loop solution gives you more explicit control over the pattern, while the string-based solution is shorter and demonstrates string concatenation and slicing.

# Inverted Left-Angle Triangle

**Challenge**

Easy

Write a program that prints an **Inverted Left-Angle Triangle** of stars as shown below. The pattern consists of 6 rows and 6 columns.

#### *Output Pattern:*

```text
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
```

**Hints**

Hint 1

1. Use nested loops—one for controlling rows and one for controlling columns—to manage where characters (stars and spaces) are placed.
2. Inside the inner loops, use print statements to output stars (`*`) and spaces based on the current row and column indices.
3. Adjust loop ranges and index calculations to ensure correct placement of stars and spaces according to the pattern's requirements.
4. Utilize formatting techniques such as print statements to control spacing and line breaks between rows of the pattern.

## Solution 1: Using the Hint (Nested Loops)

```python
for i in range(6):
    for j in range(i):
        print(" ", end=" ")

    for j in range(6 - i):
        print("*", end=" ")

    print()
```

### Explanation of Solution 1

This solution uses **nested loops** to control the spaces and stars in each row.

- `for i in range(6):` repeats the process 6 times, creating 6 rows.
- `for j in range(i):` prints spaces before the stars. As `i` increases, the number of spaces increases.
- `print(" ", end=" ")` prints a space without moving to a new line. The `end=" "` argument keeps the output on the same line.
- `for j in range(6 - i):` prints the stars. Each new row contains one fewer star.
- `print()` moves to the next line after each row is complete.

The first row has 6 stars and no leading spaces. The last row has 1 star and 5 pairs of leading spaces.

## Solution 2

```python
spaces = ""
stars = "* * * * * *"

for i in range(6):
    print((spaces * 2) + stars)
    stars = stars[:-2]
    spaces += " "
```

### Explanation of Solution 2

This solution uses **string manipulation** instead of nested loops.

- `spaces = ""` initializes an empty string to hold the leading spaces.
- `stars = "* * * * * *"` stores the initial pattern of 6 stars separated by spaces.
- `for i in range(6):` repeats the process 6 times.
- `print((spaces * 2) + stars)` prints the leading spaces followed by the current star pattern.
  - `spaces * 2` doubles the number of spaces at the beginning of each row.
  - `+ stars` joins the leading spaces and the star pattern into one string.
- `stars = stars[:-2]` removes the last two characters from the star string: the final `*` and its preceding space. This leaves one fewer star for the next row.
- `spaces += " "` adds one space to the `spaces` string. On the next iteration, `spaces * 2` adds two more leading spaces.

### Key Takeaways

- **Solution 1** uses nested loops to decide how many spaces and stars to print in each row.
- **Solution 2** builds the pattern by modifying two strings: one for spaces and one for stars.
- Both solutions produce the same inverted left-angle triangle.
- The nested-loop approach is useful for practicing loops and pattern logic, while the string-manipulation approach is concise and easy to follow.
