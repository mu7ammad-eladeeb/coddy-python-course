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

# Rhombus Pattern

## Challenge

**Difficulty:** Easy

Write a program that prints a **rhombus pattern** of stars as shown below. The pattern consists of **6 rows and 6 columns**.

### Output Pattern

```text
     * * * * * *
    * * * * * *
   * * * * * *
  * * * * * *
 * * * * * *
* * * * * *
```

## Hints

1. Use nested loops to control the placement of spaces and stars. One loop manages rows, while others handle spaces and stars within each row.
2. Inside the outer loop, use another loop to print spaces before printing stars. Adjust loop parameters to ensure proper alignment.
3. Use a loop to print stars after spaces. Maintain consistency in spacing and format.

## Solution 1: Using Nested Loops

```python
rows = 6
columns = 6

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")

    for k in range(columns):
        print("*", end=" ")

    print()
```

### Explanation

1. **`rows = 6`** sets the number of rows in the pattern.
2. **`columns = 6`** sets the number of stars in each row.
3. **`for i in range(rows)`** repeats the process six times, once for each row.
4. **`for j in range(rows - i - 1)`** prints the leading spaces. The number of spaces decreases by one on each row.
5. **`for k in range(columns)`** prints six stars on every row.
6. **`print("*", end=" ")`** prints each star followed by a space without moving to a new line.
7. **`print()`** moves to the next line after each row is complete.

The result is a slanted square shape because each row contains six stars, while the leading spaces decrease from five to zero.

## Solution 2: Using String Repetition

```python
spaces = 5
stars = "* * * * * *"

for i in range(6):
    print(" " * spaces + stars)
    spaces -= 1
```

### Explanation

1. **`spaces = 5`** initializes the number of leading spaces for the first row.
2. **`stars = "* * * * * *"`** stores the six stars and the spaces between them as a single string.
3. **`for i in range(6)`** repeats the process six times.
4. **`" " * spaces`** repeats the space character according to the current value of `spaces`.
5. **`+ stars`** concatenates the leading spaces with the star pattern.
6. **`spaces -= 1`** decreases the number of leading spaces by one after each row.

### How the Pattern Changes

| Row | Leading spaces | Stars |
|---:|---:|---:|
| 1 | 5 | 6 |
| 2 | 4 | 6 |
| 3 | 3 | 6 |
| 4 | 2 | 6 |
| 5 | 1 | 6 |
| 6 | 0 | 6 |

## Key Takeaway

Both solutions produce the same rhombus pattern:

- **Solution 1** uses nested loops to print spaces and stars separately.
- **Solution 2** uses string repetition and concatenation to build each row more concisely.

The main idea is to keep the number of stars constant while decreasing the leading spaces by one on every row.

# Pyramid of Stars

## Challenge

**Difficulty:** Easy

Write a program that prints a **pyramid pattern** of stars as shown below. The pattern consists of **6 rows and 11 columns**.

### Output Pattern

```text
           *
         * * *
       * * * * *
     * * * * * * *
   * * * * * * * * *
 * * * * * * * * * * *
```

## Hints

1. Use an outer loop to manage rows and nested inner loops to handle spaces and stars within each row.
2. The first inner loop controls the number of spaces printed before the stars:

   ```python
   for j in range(2 * (rows - i) - 1):
       print(" ", end="")
   ```

3. The second inner loop prints stars (`*`) followed by a space:

   ```python
   for k in range(2 * i + 1):
       print("*", end=" ")
   ```

## Solution 1: Using Nested Loops (Hint Solution)

```python
rows = 6

for i in range(rows):
    for j in range(2 * (rows - i) - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        print("*", end=" ")

    print()
```

### Explanation

1. **`rows = 6`** sets the number of rows in the pyramid.
2. **`for i in range(rows)`** repeats the process six times. The variable `i` goes from `0` to `5`.
3. **`for j in range(2 * (rows - i) - 1)`** controls the leading spaces. The number of spaces decreases by two on each row:
   - Row 1: 11 spaces
   - Row 2: 9 spaces
   - Row 3: 7 spaces
   - Row 4: 5 spaces
   - Row 5: 3 spaces
   - Row 6: 1 space
4. **`for k in range(2 * i + 1)`** controls the number of stars. It generates an odd number of stars on each row: 1, 3, 5, 7, 9, and 11.
5. **`print("*", end=" ")`** prints a star followed by a space without moving to a new line.
6. **`print()`** moves to the next line after completing each row.

### How the Pattern Is Created

| Row (`i`) | Leading spaces | Number of stars |
|---:|---:|---:|
| 0 | 11 | 1 |
| 1 | 9 | 3 |
| 2 | 7 | 5 |
| 3 | 5 | 7 |
| 4 | 3 | 9 |
| 5 | 1 | 11 |

The leading spaces decrease by two, while the number of stars increases by two on every row.

## Solution 2: Using String Repetition and Concatenation

```python
spaces = 11
stars = "*"

for row in range(6):
    print((spaces * " ") + stars)
    stars += " * *"
    spaces -= 2
```

### Explanation

1. **`spaces = 11`** initializes the number of leading spaces for the first row.
2. **`stars = "*"`** initializes the pattern with one star.
3. **`for row in range(6)`** repeats the process six times.
4. **`spaces * " "`** repeats the space character 11 times initially.
5. **`+ stars`** concatenates the leading spaces with the current star pattern.
6. **`stars += " * *"`** adds two more stars, with spaces between them, to the pattern for the next row.
7. **`spaces -= 2`** decreases the number of leading spaces by two after each row.

### How String Concatenation Builds the Pyramid

The `stars` variable changes on every iteration:

| Row | Value of `stars` |
|---:|---|
| 1 | `*` |
| 2 | `* * *` |
| 3 | `* * * * *` |
| 4 | `* * * * * * *` |
| 5 | `* * * * * * * * *` |
| 6 | `* * * * * * * * * * *` |

At the same time, `spaces` decreases by two:

| Row | Leading spaces |
|---:|---:|
| 1 | 11 |
| 2 | 9 |
| 3 | 7 |
| 4 | 5 |
| 5 | 3 |
| 6 | 1 |

This creates the pyramid shape by expanding the stars outward while shifting each row to the left.

## Key Takeaways

Both solutions produce the same pyramid pattern, but they use different approaches:

- **Solution 1** uses nested loops to control spaces and stars separately.
- **Solution 2** builds the pattern using string concatenation and repetition.

The main idea behind a pyramid pattern is:

- The number of leading spaces decreases by two on each row.
- The number of stars increases by two on each row.
- The number of stars is always odd: 1, 3, 5, 7, 9, and 11.

# Inverted Pyramid

## Challenge

**Difficulty:** Easy

Write a program that prints an **inverted pyramid pattern** of stars as shown below. The pattern consists of **6 rows and 11 columns**.

### Output Pattern

```text
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
```

## Hints

1. Use nested loops to control rows and columns:

   ```python
   for i in range(rows):
       for j in range(2 * i):
           # Print leading spaces

       for k in range(2 * (rows - i) - 1):
           # Print stars
   ```

2. Inside the outer loop (`i`), use an inner loop (`j`) to print leading spaces based on the current row index.
3. Inside the outer loop (`i`), use another inner loop (`k`) to print stars (`*`) with appropriate spacing based on the current row index.

## Solution 1: Using Nested Loops (Hint Solution)

```python
rows = 6

for i in range(rows):
    for j in range(2 * i):
        print(" ", end="")

    for k in range(2 * (rows - i) - 1):
        print("*", end=" ")

    print()
```

### Explanation

1. **`rows = 6`** sets the number of rows in the inverted pyramid.
2. **`for i in range(rows)`** repeats the process six times. The variable `i` goes from `0` to `5`.
3. **`for j in range(2 * i)`** prints the leading spaces. Each row adds two more spaces:
   - Row 1: 0 spaces
   - Row 2: 2 spaces
   - Row 3: 4 spaces
   - Row 4: 6 spaces
   - Row 5: 8 spaces
   - Row 6: 10 spaces
4. **`for k in range(2 * (rows - i) - 1)`** determines how many stars to print. The number of stars decreases by two on each row:
   - Row 1: 11 stars
   - Row 2: 9 stars
   - Row 3: 7 stars
   - Row 4: 5 stars
   - Row 5: 3 stars
   - Row 6: 1 star
5. **`print("*", end=" ")`** prints each star followed by a space without moving to a new line.
6. **`print()`** moves to the next line after completing each row.

## Solution 2: Using String Slicing

```python
stars = "* * * * * * * * * * *"
spaces = 0

for row in range(6):
    print((spaces * " ") + stars)
    stars = stars[:-4]
    spaces += 2
```

### Explanation

1. **`stars = "* * * * * * * * * * *"`** initializes the pattern with 11 stars separated by spaces.
2. **`spaces = 0`** initializes the number of leading spaces for the first row.
3. **`for row in range(6)`** repeats the process six times.
4. **`print((spaces * " ") + stars)`** prints the current number of leading spaces followed by the current star pattern.
5. **`stars = stars[:-4]`** removes the last four characters from the star string:
   - One star (`*`)
   - One space before it
   - Another star (`*`)

   This effectively removes two stars and their separator, leaving the remaining pattern shorter by two stars.
6. **`spaces += 2`** adds two leading spaces for the next row, shifting the pattern to the right.

### How String Slicing Changes the Pattern

| Row | Number of leading spaces | Number of stars |
|---:|---:|---:|
| 1 | 0 | 11 |
| 2 | 2 | 9 |
| 3 | 4 | 7 |
| 4 | 6 | 5 |
| 5 | 8 | 3 |
| 6 | 10 | 1 |

## Connecting Your Solution to the Hint Formulas

The formulas used in the hint solution can be calculated directly from the behavior of your string-based solution.

### 1. Leading Spaces Formula

In your solution:

```python
spaces = 0
spaces += 2
```

The number of spaces starts at `0` and increases by `2` on every iteration.

Since the row index `i` starts at `0`, the formula is:

```python
2 * i
```

This is exactly the hint's formula:

```python
for j in range(2 * i):
```

The loop prints `2 * i` spaces.

### 2. Number of Stars Formula

In your solution, the initial pattern contains 11 stars, and you remove two stars on every iteration.

The number of stars therefore follows this sequence:

```text
11, 9, 7, 5, 3, 1
```

Since there are 6 rows, the initial number of stars is:

```python
2 * rows - 1
```

Every iteration removes two stars, so the formula becomes:

```python
2 * rows - 1 - 2 * i
```

We can rearrange it:

```python
2 * (rows - i) - 1
```

This is exactly the hint's formula:

```python
for k in range(2 * (rows - i) - 1):
```

### Formula Comparison

| Pattern component | Your solution | Hint formula |
|---|---|---|
| Leading spaces | Start at 0, add 2 | `2 * i` |
| Number of stars | Start at 11, remove 2 | `2 * (rows - i) - 1` |

## Key Takeaways

Both solutions create the same inverted pyramid, but they approach the problem differently:

- **Solution 1** calculates the number of spaces and stars using formulas inside nested loops.
- **Solution 2** builds the pattern by modifying two strings: adding leading spaces and shortening the star string.

**Important:** The hint formulas are not arbitrary. They are mathematical expressions describing the exact changes happening in your solution:

- `2 * i` represents the increasing leading spaces.
- `2 * (rows - i) - 1` represents the decreasing number of stars.

Notice that you can get the formulas from the second solution numbers. Understanding how to derive these formulas from a working solution is a useful way to become more comfortable with nested loops and pattern problems.

# Diamond Pattern

## Challenge

**Difficulty:** Easy

Write a program that prints a **diamond pattern** of stars as shown below. The pattern consists of **6 rows in the upper half and 5 rows in the lower half**, making a total of 11 rows and 11 columns.

### Expected Output Pattern

```text
           *
         * * *
       * * * * *
     * * * * * * *
   * * * * * * * * *
 * * * * * * * * * * *
   * * * * * * * * *
     * * * * * * *
       * * * * *
         * * *
           *
```

## Hints

### Hint 1: Use Conditional Statements

Use conditional statements (`if-else`) to dynamically assign values based on the current row number.

Example:

```python
if i < n:
    comp = 2 * (n - i) - 1
else:
    comp = 2 * (i - n + 1) + 1
```

### Hint 2: Print Leading Spaces

Print leading spaces dynamically before printing stars.

```python
print(" " * comp, end="")
```

### Hint 3: Print Stars

Print stars (`*`) using a loop or repeated print statements to form the desired pattern.

```python
print("* " * (2 * n - comp), end="")
```

### Hint 4: Move to the Next Line

Use `print()` after printing each row of stars to move to the next line and maintain the pattern structure.

## Solution 1: Using the Hint (If-Else Statements)

This solution uses one loop for the entire diamond. An `if-else` statement determines whether the current row belongs to the upper or lower half.

```python
rows = 6

for i in range(2 * rows - 1):
    if i < rows:
        comp = 2 * (rows - i) - 1
    else:
        comp = 2 * (i - rows + 1) + 1

    print(" " * comp, end="")
    print("* " * (2 * rows - comp))
```

### Explanation

1. **`rows = 6`** sets the number of rows in the upper half of the diamond.
2. **`for i in range(2 * rows - 1)`** runs 11 times, creating 11 rows in total.
3. **`if i < rows`** checks whether the current row belongs to the upper half.
   - If true, `comp = 2 * (rows - i) - 1` calculates the leading spaces. They decrease as the pyramid grows.
4. **`else`** handles the lower half.
   - `comp = 2 * (i - rows + 1) + 1` calculates the leading spaces. They increase as the pyramid shrinks.
5. **`print(" " * comp, end="")`** prints the calculated leading spaces without moving to a new line.
6. **`print("* " * (2 * rows - comp))`** calculates and prints the stars. Their number increases in the upper half and decreases in the lower half.
7. The second `print()` automatically moves to the next line.

### How the `comp` Variable Works

| Row (`i`) | Half | `comp` (spaces) | Number of stars |
|---:|---|---:|---:|
| 0 | Upper | 11 | 1 |
| 1 | Upper | 9 | 3 |
| 2 | Upper | 7 | 5 |
| 3 | Upper | 5 | 7 |
| 4 | Upper | 3 | 9 |
| 5 | Upper | 1 | 11 |
| 6 | Lower | 3 | 9 |
| 7 | Lower | 5 | 7 |
| 8 | Lower | 7 | 5 |
| 9 | Lower | 9 | 3 |
| 10 | Lower | 11 | 1 |

**Important:** The `comp` variable represents the number of leading spaces. The expression `2 * rows - comp` calculates the number of stars.

## Solution 2: Using Nested Loops (Upper and Lower Halves)

This solution separates the diamond into two parts: an upper pyramid and a lower inverted pyramid.

```python

rows = 6

# Upper half of the diamond
for i in range(6):
    for j in range(2 * (rows - i) - 1):
        print(" ", end="")

    for k in range(i * 2 + 1):
        print("*", end=" ")

    print()

# Lower half of the diamond
for i in range(1, 6):
    for j in range(i * 2 + 1):
        print(" ", end="")

    for k in range(2 * (rows - i) - 1):
        print("*", end=" ")

    print()
```

### Explanation

The diamond consists of two parts:

1. **Upper half:** The number of stars increases on each row, while the leading spaces decrease.
2. **Lower half:** The number of stars decreases on each row, while the leading spaces increase.

#### Upper Half

```python
for i in range(6):
    for j in range(2 * (rows - i) - 1):
        print(" ", end="")

    for k in range(i * 2 + 1):
        print("*", end=" ")

    print()
```

- **`for i in range(6)`** creates the six rows of the upper half.
- **`2 * (rows - i) - 1`** calculates the number of leading spaces. It decreases by two on each row.
- **`i * 2 + 1`** calculates the number of stars. It increases by two on each row.
- **`print("*", end=" ")`** prints stars on the same line, with a space after each star.
- **`print()`** moves to the next row.

#### Lower Half

```python
for i in range(1, 6):
    for j in range(i * 2 + 1):
        print(" ", end="")

    for k in range(2 * (rows - i) - 1):
        print("*", end=" ")

    print()
```

- **`for i in range(1, 6)`** creates the five rows of the lower half. We start at `1` because the widest row has already been printed in the upper half.
- **`i * 2 + 1`** calculates the leading spaces. They increase by two on each row.
- **`2 * (rows - i) - 1`** calculates the number of stars. They decrease by two on each row.
- **`print()`** moves to the next row.

### How the Pattern Changes

| Part | Row | Leading spaces | Number of stars |
|---|---:|---:|---:|
| Upper | 1 | 11 | 1 |
| Upper | 2 | 9 | 3 |
| Upper | 3 | 7 | 5 |
| Upper | 4 | 5 | 7 |
| Upper | 5 | 3 | 9 |
| Upper | 6 | 1 | 11 |
| Lower | 1 | 3 | 9 |
| Lower | 2 | 5 | 7 |
| Lower | 3 | 7 | 5 |
| Lower | 4 | 9 | 3 |
| Lower | 5 | 11 | 1 |

## Solution 3: Using String Repetition and Slicing

This solution builds the upper half by adding stars and removing leading spaces. Then it builds the lower half by removing stars and adding leading spaces.

```python
stars = "*"
spaces = 11

# Upper half
for row in range(6):
    print((spaces * " ") + stars)

    if spaces == 1:
        break

    stars += " * *"
    spaces -= 2

# Lower half
for row in range(5):
    stars = stars[:-4]
    spaces += 2
    print((spaces * " ") + stars)
```

### Explanation

#### Initial Values

```python
stars = "*"
spaces = 11
```

- **`stars = "*"`** starts with one star.
- **`spaces = 11`** starts with 11 leading spaces.

#### Building the Upper Half

```python
for row in range(6):
    print((spaces * " ") + stars)

    if spaces == 1:
        break

    stars += " * *"
    spaces -= 2
```

1. **`print((spaces * " ") + stars)`** prints the current leading spaces followed by the star pattern.
2. **`if spaces == 1:`** checks whether we have reached the widest row.
3. **`break`** stops the loop after printing the widest row. This prevents adding more stars when the upper half is complete.
4. **`stars += " * *"`** adds two stars to the pattern, including the spaces between them.
5. **`spaces -= 2`** removes two leading spaces before the next row.

The upper half grows like this:

| Row | Stars | Leading spaces |
|---:|---|---:|
| 1 | `*` | 11 |
| 2 | `* * *` | 9 |
| 3 | `* * * * *` | 7 |
| 4 | `* * * * * * *` | 5 |
| 5 | `* * * * * * * * *` | 3 |
| 6 | `* * * * * * * * * * *` | 1 |

#### Building the Lower Half

```python
for row in range(5):
    stars = stars[:-4]
    spaces += 2
    print((spaces * " ") + stars)
```

1. **`stars = stars[:-4]`** removes the last four characters from the star string. This removes two stars and their separating spaces.
2. **`spaces += 2`** adds two leading spaces, shifting the pattern to the right.
3. **`print((spaces * " ") + stars)`** prints the shortened star pattern with the increased leading spaces.

The lower half shrinks like this:

| Row | Stars | Leading spaces |
|---:|---|---:|
| 1 | `* * * * * * * * *` | 3 |
| 2 | `* * * * * * *` | 5 |
| 3 | `* * * * *` | 7 |
| 4 | `* * *` | 9 |
| 5 | `*` | 11 |

## Connecting the Three Solutions

All three solutions follow the same mathematical pattern, even though they use different techniques.

| Pattern component | Hint solution | Nested-loop solution | String-based solution |
|---|---|---|---|
| Upper leading spaces | `2 * (rows - i) - 1` | `2 * (rows - i) - 1` | Start at 11, subtract 2 |
| Upper stars | `2 * rows - comp` | `2 * i + 1` | Add `" * *"` |
| Lower leading spaces | `2 * (i - rows + 1) + 1` | `i * 2 + 1` | Add 2 |
| Lower stars | `2 * rows - comp` | `2 * (rows - i) - 1` | Remove 4 characters using `[:-4]` |

The formulas in the first two solutions describe the same changes that the string-based solution performs step by step.

## Key Takeaways

- A diamond pattern consists of an upper pyramid and a lower inverted pyramid.
- In the upper half, stars increase while leading spaces decrease.
- In the lower half, stars decrease while leading spaces increase.
- **Solution 1** uses `if-else` statements to handle both halves in one loop.
- **Solution 2** uses nested loops to calculate and print spaces and stars separately.
- **Solution 3** uses string concatenation and slicing to build the pattern by modifying existing strings.

**Important:** Understanding how the formulas in the hint solution describe the changes in your string-based solution helps you develop a stronger understanding of loops, conditions, and pattern problems.


# Right Direction Arrow

## Challenge

**Difficulty:** Easy

Write a program that prints a **Right Direction Arrow** of stars as shown below. The pattern consists of **11 rows and 6 columns**.

### Expected Output Pattern

```text
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * *   
* * * * * 
* * * * 
* * * 
* * 
* 
```

## Hints

Use two loops—one for the upper half and one for the lower half—to create a symmetric pattern.

1. In the first loop (`for i in range(n):`), increase the number of stars per line using `"* " * (i + 1)`.
2. In the second loop (`for i in range(n - 1):`), decrease the number of stars per line using `"* " * (n - i - 1)`.
3. Print stars using `"* "` to maintain alignment and create the desired pattern.

## Solution 1: Using the Hint

```python
n = 6

# Upper half: increase the number of stars
for i in range(n):
    print("* " * (i + 1))

# Lower half: decrease the number of stars
for i in range(n - 1):
    print("* " * (n - i - 1))
```

### Explanation

We use two separate loops to create the arrow's symmetric shape.

**1. Upper half**

```python
for i in range(n):
    print("* " * (i + 1))
```

- `range(n)` repeats the loop 6 times.
- `i + 1` determines how many stars are printed on each row.
- The number of stars increases from 1 to 6.

**2. Lower half**

```python
for i in range(n - 1):
    print("* " * (n - i - 1))
```

- `range(n - 1)` repeats the loop 5 times.
- `n - i - 1` decreases the number of stars on each row.
- The number of stars decreases from 5 to 1.

The two loops produce 11 rows in total: 6 rows in the upper half and 5 in the lower half.

## Solution 2: Using If Statements and a Counter

```python
rows = 11
stars = 1

for i in range(rows):
    if i < 5:
        print("* " * stars)
        stars += 1

    if i >= 5:
        print("* " * stars)
        stars -= 1
```

### Explanation

This solution uses one loop, two `if` statements, and a variable named `stars` to control the number of stars printed.

**1. Initialize the variables**

```python
rows = 11
stars = 1
```

- `rows = 11` means the loop will run 11 times.
- `stars = 1` means the first row starts with one star.

**2. Create the upper half**

```python
if i < 5:
    print("* " * stars)
    stars += 1
```

- `i < 5` identifies the first five iterations (`i` goes from 0 to 4).
- `print("* " * stars)` prints the current number of stars.
- `stars += 1` increases the number of stars by one after each row.

The upper half prints 1, 2, 3, 4, and 5 stars.

**3. Create the middle and lower half**

```python
if i >= 5:
    print("* " * stars)
    stars -= 1
```

- `i >= 5` identifies the remaining six iterations (`i` goes from 5 to 10).
- The first time this condition is true, `stars` is 6, so the middle row prints 6 stars.
- `stars -= 1` decreases the number of stars by one after each row.

The lower half prints 6, 5, 4, 3, 2, and 1 stars.

**Note:** The middle row belongs to the second condition, which is why the first condition uses `i < 5` rather than `i <= 5`.

## Key Takeaways

- Use two loops when you want to build an increasing and decreasing pattern separately.
- Use one loop with conditions when you want to control different stages of a pattern.
- The `"* " * stars` expression repeats the star string according to the value of `stars`.
- The `+= 1` operator increases a variable by one, while `-= 1` decreases it by one.
- Both solutions produce the same 11-row arrow pattern.


# Left Direction Arrow

## Challenge

**Difficulty:** Easy

Write a program that prints a **Left Direction Arrow** of stars as shown below. The pattern consists of **11 rows and 6 columns**.

### Expected Output Pattern

```text
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
```

## Hints

**Hint 1: Use two loops**

- Use two loops: one for the upper half and one for the lower half of the pattern.
- You can use a loop for rows and a nested loop for columns to manage star placement.

**Hint 2: Control spaces and stars**

- Use `" "` for spaces and `"* "` for stars to control formatting.
- Combine spaces and stars to align the stars correctly within each row.
- Print stars incrementally in the upper half of the pattern, starting with fewer stars and increasing their count as you move down the rows.

**Hint 3: Reverse the star pattern**

- Decrease the number of stars as you move down the rows after the midpoint.
- The lower half should be the reverse of the upper half, excluding the middle row.

## Solution: Using Two Loops

```python
n = 6

# Upper half: increase stars and decrease spaces
for i in range(n):
    print("  " * (n - i - 1) + "* " * (i + 1))

# Lower half: decrease stars and increase spaces
for i in range(n - 1):
    print("  " * (i + 1) + "* " * (n - i - 1))
```

## Explanation

The pattern is made up of two parts:

1. **Upper half:** The number of stars increases from 1 to 6, while the number of leading spaces decreases.
2. **Lower half:** The number of stars decreases from 5 to 1, while the number of leading spaces increases.

### 1. Initialize the variable

```python
n = 6
```

The variable `n` represents the maximum number of stars in the middle row.

### 2. Create the upper half

```python
for i in range(n):
    print("  " * (n - i - 1) + "* " * (i + 1))
```

- `range(n)` repeats the loop 6 times.
- `"  " * (n - i - 1)` prints the leading spaces. The number of spaces decreases with each row.
- `"* " * (i + 1)` prints the stars. The number of stars increases with each row.

For example:

| `i` | Leading spaces | Stars |
|---:|---:|---:|
| 0 | 5 pairs | 1 |
| 1 | 4 pairs | 2 |
| 2 | 3 pairs | 3 |
| 3 | 2 pairs | 4 |
| 4 | 1 pair | 5 |
| 5 | 0 pairs | 6 |

### 3. Create the lower half

```python
for i in range(n - 1):
    print("  " * (i + 1) + "* " * (n - i - 1))
```

- `range(n - 1)` repeats the loop 5 times because the middle row has already been printed.
- `"  " * (i + 1)` increases the leading spaces with each row.
- `"* " * (n - i - 1)` decreases the number of stars with each row.

This produces 5, 4, 3, 2, and 1 stars.

## Key Takeaways

- Use two loops to create the increasing and decreasing halves of a pattern.
- Use `"  "` to create two-character indentation spaces, keeping the stars aligned.
- Use `"* "` to print stars with consistent spacing.
- `n - i - 1` decreases the number of stars or leading spaces as the loop progresses.
- The middle row is printed only once, so the final pattern contains exactly 11 rows.


# Plus Pattern

## Challenge

**Difficulty:** Easy

Write a program that prints a **Plus Pattern** of stars as shown below. The pattern consists of **7 rows and 7 columns**.

### Expected Output Pattern

```text
   *   
   *   
   *   
*******
   *   
   *   
   *
```

## Hints

1. Use nested loops to iterate through rows and columns to control where stars (`*`) and spaces (`" "`) are placed.
2. Use an `if` statement inside the inner loop to decide whether to print a star (`*`) or a space (`" "`).
3. Adjust the loop variables (`row` and `col`) to control the size and shape of the pattern.
4. Use `print()` with appropriate arguments to control new lines and ensure the pattern is formatted correctly.

## Solution 1: Using the Hint (Nested Loops)

```python
size = 7

for row in range(size):
    for col in range(size):
        if row == 3 or col == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

### Explanation

This solution uses two nested loops to create the plus sign.

**1. Initialize the size**

```python
size = 7
```

The pattern has 7 rows and 7 columns, so we use `size = 7`.

**2. Loop through the rows and columns**

```python
for row in range(size):
    for col in range(size):
```

- The outer loop controls the rows.
- The inner loop controls the columns.
- Both loops run 7 times, creating a 7 × 7 pattern.

**3. Decide where to print stars**

```python
if row == 3 or col == 3:
    print("*", end="")
else:
    print(" ", end="")
```

The condition checks two things:

- `row == 3`: If the current row is the fourth row (the middle row), print a star in every column. This creates the horizontal line.
- `col == 3`: If the current column is the fourth column (the middle column), print a star in every row. This creates the vertical line.

The `or` operator means that either condition can be true for a star to be printed.

If neither condition is true, a space is printed.

**4. Move to the next row**

```python
print()
```

This statement is outside the inner loop, so it runs after all 7 columns have been processed. It moves the output to the next line.

## Solution 2: Using One Loop and If Statements

```python
rows = 13

for i in range(rows, 0, -1):
    if (i < 7 or i > 7) and i % 2 == 1:
        print("   *", end='')

    if (i < 7 or i > 7) and i % 2 == 0:
        print()

    if i == 7:
        print("*******", end='')
```

### Explanation

This solution uses one loop, three `if` statements, and the remainder operator (`%`) to create the plus pattern.

**1. Initialize the number of iterations**

```python
rows = 13
```

We use 13 iterations because the loop needs to alternate between printing a vertical star and moving to a new line, with one special iteration for the horizontal line.

**2. Loop backward from 13 to 1**

```python
for i in range(rows, 0, -1):
```

- `rows` is the starting value (13).
- `0` is the stopping value, which is excluded.
- `-1` decreases `i` by one each time.

Therefore, `i` takes the values from 13 down to 1.

**3. Print the upper and lower vertical lines**

```python
if (i < 7 or i > 7) and i % 2 == 1:
    print("   *", end='')
```

This condition has two parts:

- `(i < 7 or i > 7)` checks that `i` is not equal to 7. This excludes the middle iteration because it will print the horizontal line.
- `i % 2 == 1` checks whether `i` is odd.

When both conditions are true, the program prints three spaces followed by a star.

The `end=''` argument prevents `print()` from automatically moving to a new line. This allows the next condition to control the line break.

**4. Move to the next line**

```python
if (i < 7 or i > 7) and i % 2 == 0:
    print()
```

This condition checks whether `i` is even and not equal to 7.

When it is true, `print()` moves the output to a new line.

This works together with the previous condition:
- Odd values print the vertical star.
- The following even values move to the next line.

**5. Print the horizontal line**

```python
if i == 7:
    print("*******", end='')
```

When `i` reaches 7, the program prints seven consecutive stars.

This creates the horizontal part of the plus sign.

The next iteration has `i = 6`, so the second condition executes and moves the output to a new line before the lower vertical stars are printed.

### Understanding the Loop

| Value of `i` | Action |
|---:|---|
| 13 | Print vertical star |
| 12 | Move to next line |
| 11 | Print vertical star |
| 10 | Move to next line |
| 9 | Print vertical star |
| 8 | Move to next line |
| 7 | Print horizontal stars |
| 6 | Move to next line |
| 5 | Print vertical star |
| 4 | Move to next line |
| 3 | Print vertical star |
| 2 | Move to next line |
| 1 | Print vertical star |

The result is three vertical stars above the horizontal line, one horizontal line of seven stars, and three vertical stars below it.

## Key Takeaways

- Nested loops can be used to control the position of every character in a pattern.
- The `or` operator allows a condition to be true when either of two expressions is true.
- The modulo operator (`%`) gives the remainder after division. `i % 2 == 1` identifies odd numbers, while `i % 2 == 0` identifies even numbers.
- `end=''` prevents `print()` from automatically starting a new line.
- An empty `print()` moves the output to the next line.
- Both solutions create the same plus pattern using different approaches.
