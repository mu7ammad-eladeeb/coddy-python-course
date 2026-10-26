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
