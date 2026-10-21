# **Prerequisites**

Welcome to the **Quiz Generator** project using Python.

In order to ace this course, you must have a good knowledge of the Python programming language, and more specifically, **Object-Oriented Programming (OOP)** concepts, such as classes, methods, and so on.

But don't worry! We will take you step by step and give you all the tools you need to create this great project.

**Happy Coding!**

# **The Project**


Before we start let's discuss what you are going to create.

In this course you will create a **Quiz Generator application**:

You will use OOP concepts to create different Question objects - Open question, Multi options question and Yes/No question.
You will create main class Quiz which will coordinate the quiz
The user which takes the quiz will be able to answer the questions and in the end, results will be shown
Sounds exciting? **Let's gooo!**


# **Question**

Example of an abstract class with two abstract methods:

```python
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self, a, b):
        pass
```

## **Challenge**

Easy

Create an **abstract class** named **`Question`** with the following methods:

- **`print`** — an abstract method that takes no input.
- **`check`** — an abstract method that takes a string (the answer typed by the user) as input.

## **Solution**

```python
from abc import ABC, abstractmethod


class Question(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def check(self, answer: str):
        pass
```

## **Explanation of the solution:**

1. **Import `ABC` and `abstractmethod`:**
   - `ABC` is the base class used to define abstract classes.
   - `abstractmethod` is a decorator that marks a method as abstract.

2. **Create the `Question` class:**

   ```python
   class Question(ABC):
   ```

   Inheriting from `ABC` makes `Question` an abstract base class.

3. **Define the `print` method:**

   ```python
   @abstractmethod
   def print(self):
       pass
   ```

   The `@abstractmethod` decorator requires subclasses to implement this method. It takes no explicit arguments besides `self`, which Python passes automatically to instance methods.

4. **Define the `check` method:**

   ```python
   @abstractmethod
   def check(self, answer: str):
       pass
   ```

   This method accepts an `answer` string representing the user's response. The `: str` annotation indicates the expected type but does not enforce it at runtime.

5. **Why use `pass`?**

   `pass` is a placeholder indicating that the method has no implementation in the abstract class. Subclasses must provide implementations of both abstract methods before their instances can be created.

**Example of implementation:**

```python
class MultipleChoiceQuestion(Question):
    def print(self):
        print("What is 2 + 2?")

    def check(self, answer: str):
        return answer == "4"


question = MultipleChoiceQuestion()
question.print()
print(question.check("4"))
```

**Output:**

```text
What is 2 + 2?
True
```

## **Key takeaway:**

An abstract class defines a common interface that its subclasses must follow. The `Question` class requires every concrete subclass to implement both `print()` and `check()`, while allowing each subclass to define its own behavior.


# Yes/No Question

## Challenge

**Difficulty:** Easy

Create a class **`YesNoQuestion`** that inherits from **`Question`** and implements the constructor and the methods **`print`** and **`check`** from the `Question` class.

### Constructor

The constructor should accept a string and a boolean and save them under the fields **`question`** and **`answer`**, respectively.

### `print` Method

Prints the question in the format **`'[?] {question} (yes/no)'`**.

For example, if the question is `'Are you experienced programmer?'`, the method should print:

```text
[?] Are you experienced programmer? (yes/no)
```

### `check` Method

Returns `True` if the input string is `'yes'` and the `answer` field is `True`, or if the input string is `'no'` and the `answer` field is `False`. Otherwise, it returns `False`.

---

## Solution

```python
from abc import ABC, abstractmethod


class Question(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def check(self, answer: str):
        # `answer: str` is a type hint indicating that `answer`
        # is expected to be a string, but Python does not
        # enforce it at runtime.
        pass


class YesNoQuestion(Question):
    def __init__(self, question: str, answer: bool):
        self.question = question
        self.answer = answer

    def print(self):
        print(f"[?] {self.question} (yes/no)")

    def check(self, answer: str):
        return (
            (answer == "yes" and self.answer is True)
            or (answer == "no" and self.answer is False)
        )
```

## Explanation of the Solution

### 1. Importing the Required Tools

```python
from abc import ABC, abstractmethod
```

- `ABC` is a base class used to create abstract classes.
- `abstractmethod` is a decorator that marks methods as abstract, requiring subclasses to implement them.

### 2. Creating the Abstract `Question` Class

```python
class Question(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def check(self, answer: str):
        pass
```

The `Question` class defines a common structure for question types.

- `print()` must be implemented by subclasses.
- `check(answer: str)` must also be implemented by subclasses and accepts an answer expected to be a string.
- `pass` is a placeholder because the abstract methods do not provide an implementation here.

**Note:** `answer: str` is a type hint indicating that `answer` is expected to be a string, but Python does not enforce it at runtime.

### 3. Inheriting from `Question`

```python
class YesNoQuestion(Question):
```

The `YesNoQuestion` class inherits from `Question`. Since `Question` has two abstract methods, `YesNoQuestion` must implement both `print()` and `check()` before its objects can be created.

### 4. Defining the Constructor

```python
def __init__(self, question: str, answer: bool):
    self.question = question
    self.answer = answer
```

The constructor runs when a new object is created.

- `question: str` indicates that the question is expected to be a string.
- `answer: bool` indicates that the correct answer is expected to be a boolean (`True` or `False`).
- `self.question` stores the question text.
- `self.answer` stores the correct boolean answer.

### 5. Implementing the `print` Method

```python
def print(self):
    print(f"[?] {self.question} (yes/no)")
```

The f-string inserts the question text into the required format.

For example:

```python
question = YesNoQuestion("Are you experienced programmer?", True)
question.print()
```

**Output:**

```text
[?] Are you experienced programmer? (yes/no)
```

### 6. Implementing the `check` Method

```python
def check(self, answer: str):
    return (
        (answer == "yes" and self.answer is True)
        or (answer == "no" and self.answer is False)
    )
```

This cleaner version returns the boolean expression directly without creating a separate `result` variable.

- `(answer == "yes" and self.answer is True)` evaluates to `True` when the user enters `"yes"` and the stored answer is `True`.
- `(answer == "no" and self.answer is False)` evaluates to `True` when the user enters `"no"` and the stored answer is `False`.
- `or` means that either condition can make the whole expression `True`.
- If neither condition is satisfied, the method returns `False`.

**Example:**

```python
question = YesNoQuestion("Are you experienced programmer?", True)

print(question.check("yes"))
print(question.check("no"))
```

**Output:**

```text
True
False
```

Because the correct answer is `True`, entering `"yes"` returns `True`, while entering `"no"` returns `False`.

## Key Takeaway

This exercise demonstrates **abstraction and inheritance**. The abstract `Question` class defines which methods a question must have, while `YesNoQuestion` implements those methods for questions that accept `"yes"` or `"no"` as answers.


# Open Question

## Challenge

**Difficulty:** Easy

Create a class **`OpenQuestion`** which inherits from **`Question`** and implements the constructor and the methods **`print`** and **`check`** from the `Question` class.

### Constructor

The constructor should receive a string and a list of strings and save them under the fields **`question`** and **`answers`**, respectively.

### `print` Method

Prints the question in the following format:

`[?] {question}`

For example, if the question is `'Are you experienced programmer?'`, the method should print:

```text
[?] Are you experienced programmer?
```

### `check` Method

Returns `True` if the input string (the answer) is included in the `answers` field; otherwise, it returns `False`.

For example, if `answers = ['yes', 'maybe']`:

- `check('yes')` returns `True`.
- `check('nope')` returns `False`.

## Solution

```python
class OpenQuestion(Question):
    def __init__(self, question: str, answers: list[str]):
        self.question = question
        self.answers = answers

    def print(self):
        print(f"[?] {self.question}")

    def check(self, answer: str):
        return answer in self.answers
```

## Explanation of the Solution

### 1. Inheriting from `Question`

```python
class OpenQuestion(Question):
```

The `OpenQuestion` class inherits from the `Question` class. This means it must implement the abstract methods defined in `Question`, including `print` and `check`, to be instantiated.

### 2. Defining the Constructor

```python
def __init__(self, question: str, answers: list[str]):
    self.question = question
    self.answers = answers
```

The constructor receives two arguments:

- `question: str` — the question text.
- `answers: list[str]` — a list of acceptable answers.

The values are stored in instance attributes:

- `self.question` stores the question text.
- `self.answers` stores the list of acceptable answers.

The type hints indicate the expected types but do not enforce them at runtime.

### 3. Implementing the `print` Method

```python
def print(self):
    print(f"[?] {self.question}")
```

The f-string inserts the value of `self.question` into the required format.

For example:

```python
question = OpenQuestion(
    "Are you experienced programmer?",
    ["yes", "maybe"]
)

question.print()
```

Output:

```text
[?] Are you experienced programmer?
```

### 4. Implementing the `check` Method

```python
def check(self, answer: str):
    return answer in self.answers
```

The `in` operator checks whether the provided answer exists in the `answers` list.

- If the answer is found, the expression returns `True`.
- If the answer is not found, the expression returns `False`.

For example:

```python
question = OpenQuestion(
    "Are you experienced programmer?",
    ["yes", "maybe"]
)

print(question.check("yes"))
print(question.check("nope"))
```

Output:

```text
True
False
```

The comparison is case-sensitive, so `"Yes"` would not match `"yes"`.

## Key Takeaway

The `OpenQuestion` class demonstrates **inheritance and method implementation**. It inherits from `Question`, stores the question and its acceptable answers, prints the question in the required format, and uses the `in` operator to check whether an answer is accepted.



# Multiple Options Question

## Challenge

**Difficulty:** Medium

Create a class **`MultiOptionsQuestion`** which inherits from **`Question`** and implements the constructor and the methods **`print`** and **`check`** from the `Question` class.

### Constructor

The constructor should receive a string, a list of strings, and an integer, and save them under the fields **`question`**, **`options`**, and **`answer_index`**, respectively.

### `print` Method

Prints the question and its options in the following format:

```python
[?] {question}

[1] {options[0]}
[2] {options[1]}
.
.
.
```

For example, if the question is `'How many states are in the USA?'` and the options are `['49', '50', '51', '32']`, the method should print:

```text
[?] How many states are in the USA?

[1] 49
[2] 50
[3] 51
[4] 32
```

### `check` Method

Returns `True` if the input string (the answer) is equal to **`answer_index + 1`**; otherwise, it returns `False`.

**Note:** The input of the `check` method is a string, so you must cast it to an integer before comparing it with `answer_index + 1`.

## Solution

```python
class MultiOptionsQuestion(Question):
    def __init__(
        self,
        question: str,
        options: list[str],
        answer_index: int
    ):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f"[?] {self.question}\n")

        for index, option in enumerate(self.options, start=1):
            print(f"[{index}] {option}")

    def check(self, answer: str):
        return int(answer) == self.answer_index + 1
```

## Explanation of the Solution

### 1. Inheriting from `Question`

```python
class MultiOptionsQuestion(Question):
```

The `MultiOptionsQuestion` class inherits from `Question`. It must implement the abstract methods `print` and `check` so that objects of this class can be created.

### 2. Defining the Constructor

```python
def __init__(
    self,
    question: str,
    options: list[str],
    answer_index: int
):
    self.question = question
    self.options = options
    self.answer_index = answer_index
```

The constructor receives three arguments:

- `question: str` — the text of the question.
- `options: list[str]` — a list containing the possible answers.
- `answer_index: int` — the zero-based index of the correct answer.

These values are stored in the instance attributes `self.question`, `self.options`, and `self.answer_index`.

**Important:** The index starts at `0`, but the options displayed to the user start at `1`.

For example, if `answer_index = 1`, the correct answer is the second option, which is displayed as option `[2]`.

### 3. Implementing the `print` Method

```python
def print(self):
    print(f"[?] {self.question}\n")

    for index, option in enumerate(self.options, start=1):
        print(f"[{index}] {option}")
```

First, the method prints the question followed by a blank line. The `\n` character adds a line break.

Next, the `for` loop displays every option with its corresponding number.

The built-in `enumerate()` function allows us to access both the index and the option while looping through the list.

The argument `start=1` makes the numbering begin at `1` instead of the default `0`.

For example:

```python
question = MultiOptionsQuestion(
    "How many states are in the USA?",
    ["49", "50", "51", "32"],
    1
)

question.print()
```

Output:

```text
[?] How many states are in the USA?

[1] 49
[2] 50
[3] 51
[4] 32
```

### 4. Implementing the `check` Method

```python
def check(self, answer: str):
    return int(answer) == self.answer_index + 1
```

The input `answer` is a string, such as `"2"`, but `answer_index` is an integer.

The expression `int(answer)` converts the input string to an integer so that it can be compared with `self.answer_index + 1`.

We add `1` because the stored index starts at `0`, while the displayed option numbers start at `1`.

For example, if `self.answer_index = 1`:

- `check("2")` returns `True` because `2 == 1 + 1`.
- `check("1")` returns `False` because `1 != 1 + 1`.
- `check("3")` returns `False` because `3 != 1 + 1`.

Example:

```python
question = MultiOptionsQuestion(
    "How many states are in the USA?",
    ["49", "50", "51", "32"],
    1
)

print(question.check("2"))
print(question.check("1"))
```

Output:

```text
True
False
```

**Note:** `int(answer)` raises a `ValueError` if the input is not a valid integer string, such as `"hello"`. The solution assumes the input is a valid number, as required by the challenge.

## Key Takeaway

The `MultiOptionsQuestion` class demonstrates **inheritance, loops, and index conversion**.

- Inheritance allows the class to implement the interface defined by `Question`.
- `enumerate(self.options, start=1)` displays options using numbers starting at `1`.
- `int(answer)` converts the user's string input into an integer.
- `self.answer_index + 1` converts the zero-based correct-answer index into the one-based option number shown to the user.


# Start

## Challenge

**Difficulty:** Medium

Add the method **`start`** to the `Quiz` class. The method should take no additional arguments, display the questions stored in the `questions` field, and ask the user to input an answer for each question.

Use each question's **`print`** method to display it.

Each input prompt should start with **`[+] `**. Check the hint if you are not sure how to do this!

> **Note:** Pay attention to spaces and new lines!

## Hint

### Hint 1

To take input from the user, use the built-in function `input()`. To display a prefix before the user enters their answer, pass the prefix as an argument:

```python
input('[+] ')
```

## Solution

```python
class Quiz:
    def __init__(self, questions: list):
        self.questions = questions

    def start(self):
        for question in self.questions:
            question.print()
            user_answer = input('[+] ')
            print('\n')
```

## Explanation of the Solution

### 1. Creating the `Quiz` Class

```python
class Quiz:
    def __init__(self, questions: list):
        self.questions = questions
```

The constructor receives a list of question objects and stores it in `self.questions`. These objects can be instances of `YesNoQuestion`, `OpenQuestion`, or `MultiOptionsQuestion`.

### 2. Defining the `start` Method

```python
def start(self):
```

The `start` method takes only `self`, which refers to the current `Quiz` object. It does not require any additional arguments.

### 3. Looping Through the Questions

```python
for question in self.questions:
```

The loop visits every question stored in the list. During each iteration, `question` refers to one question object.

### 4. Displaying Each Question

```python
question.print()
```

The question's `print` method displays its content. Each question type implements this method according to its own format.

- `YesNoQuestion` displays the question followed by `(yes/no)`.
- `OpenQuestion` displays the question.
- `MultiOptionsQuestion` displays the question and its numbered options.

### 5. Asking for User Input

```python
user_answer = input('[+] ')
```

The built-in `input()` function displays the prompt `[+] ` and waits for the user to enter an answer.

The entered value is returned as a string and stored in `user_answer`.

**Important:** The space after `+` is intentional. The challenge requires the exact prompt `'[+] '`.

### 6. Printing Blank Lines

```python
print('\n')
```

The string `'\n'` represents a newline. Printing it adds a newline from the string itself and another from `print()`'s default behavior, producing two line breaks.

This is equivalent to:

```python
print()
print()
```

The blank lines help maintain the expected output formatting.

## Key Takeaway

The `start` method loops through the questions, displays each one using its `print` method, collects the user's answer with the required `[+] ` prompt, and prints blank lines to maintain the expected formatting.

This demonstrates **object-oriented programming and polymorphism**: the same `question.print()` call works with different question types because each class provides its own implementation.


# Print Results

Let's deal with the quiz results and print them.

## Challenge

**Difficulty:** Medium

Write a method **`print_results`** inside the `Quiz` class which receives a list of Boolean values as input. `True` means the corresponding question was answered correctly, while `False` means it was answered incorrectly.

The method should print the results in a specific format. Check the test cases to understand the expected output.

## Hint

### Hint 1

The method signature should be:

```python
def print_results(self, results):
```

Remember that this method belongs inside the **`Quiz`** class.

## Solution

```python
def print_results(self, results: list[bool]):
    true = 0
    false = 0
    leng = len(results)

    for idx, result in enumerate(results):
        if result is True:
            true += 1
        else:
            false += 1

    print(f'Your score is {true}/{leng}\n')

    for idx, result in enumerate(results):
        if result is True:
            print(f"[{idx+1}] Pass")
        else:
            print(f"[{idx+1}] Fail")
```

## Explanation of the Solution

### 1. Defining the Method and Variables

```python
def print_results(self, results: list[bool]):
    true = 0
    false = 0
    leng = len(results)
```

The method receives `results`, a list of Boolean values representing whether each question was answered correctly.

- `true` counts the correctly answered questions.
- `false` counts the incorrectly answered questions.
- `leng` stores the total number of questions by using `len(results)`.

The type hint `list[bool]` indicates that `results` is expected to be a list of Boolean values.

### 2. Counting Correct and Incorrect Answers

```python
for idx, result in enumerate(results):
    if result is True:
        true += 1
    else:
        false += 1
```

The `enumerate()` function iterates through the results and provides both the index and the current Boolean value.

For each result:

- If `result is True`, the correct-answer counter increases by one.
- Otherwise, the incorrect-answer counter increases by one.

The variable `idx` is available for the position of each result, although it is not needed for counting.

### 3. Printing the Total Score

```python
print(f'Your score is {true}/{leng}\n')
```

This f-string displays the number of correct answers over the total number of questions.

For example, if there are three questions and two were answered correctly, the output is:

```text
Your score is 2/3
```

The `\n` adds an extra newline after the score to separate it from the individual results.

### 4. Printing Each Question's Result

```python
for idx, result in enumerate(results):
    if result is True:
        print(f"[{idx+1}] Pass")
    else:
        print(f"[{idx+1}] Fail")
```

The second loop displays the result of every question.

- `idx + 1` makes the question numbering start at `1` instead of `0`.
- `Pass` is printed when the answer is correct.
- `Fail` is printed when the answer is incorrect.

For example, given:

```python
results = [True, False, True]
```

The output is:

```text
Your score is 2/3

[1] Pass
[2] Fail
[3] Pass
```

## Cleaner Solution

```python
def print_results(self, results: list[bool]):
        score = sum(results)
        total = len(results)

        print(f"Your score is {score}/{total}\n")

        for idx, passed in enumerate(results, start=1):
            status = "Pass" if passed else "Fail"
            print(f"[{idx}] {status}")
```
## Key Takeaway

The `print_results` method uses **loops, conditional statements, and counters** to summarize quiz performance.

First, it counts the correct and incorrect answers and prints the score. Then, it loops through the results again to display `Pass` or `Fail` for each question, using `idx + 1` to number the questions starting from one.

The `false` counter is included in your solution, although it is not used in the final output. The score only needs the number of correct answers and the total number of questions.


# Start and Print Results

## Challenge

**Difficulty:** Medium

Complete the quiz functionality by implementing two methods inside the `Quiz` class:

- **`start`** — displays each question, collects the user's answer, checks whether the answer is correct, stores the results, and then prints the final results.
- **`print_results`** — receives a list of Boolean values and displays the total score and the result of each question.

A result of `True` means the question was answered correctly, while `False` means it was answered incorrectly.

## Solution

```python
def start(self):
    results = []

    for question in self.questions:
        question.print()
        user_answer = input('[+] \n')
        print()
        results.append(question.check(user_answer))

    return self.print_results(results)


def print_results(self, results: list[bool]):
    score = sum(results)
    total = len(results)

    print(f"Your score is {score}/{total}\n")

    for idx, passed in enumerate(results, start=1):
        status = "Pass" if passed else "Fail"
        print(f"[{idx}] {status}")
```

## Explanation of the Solution

### 1. Initializing the Results List

```python
results = []
```

The `results` list stores the outcome of each question. Each element will be a Boolean value:

- `True` means the answer is correct.
- `False` means the answer is incorrect.

Initially, the list is empty because no questions have been answered yet.

### 2. Looping Through the Questions

```python
for question in self.questions:
```

The loop iterates through every question stored in `self.questions`. Each question is processed one at a time.

### 3. Displaying the Question

```python
question.print()
```

The question's `print()` method displays its text and, when applicable, its options.

Because each question class implements its own `print()` method, the same method call works for different question types.

### 4. Collecting the User's Answer

```python
user_answer = input('[+] \n')
```

The built-in `input()` function displays the prompt and waits for the user to enter an answer.

- `[+] ` is the required input prefix.
- `\n` adds a newline after the prompt text.

The user's input is stored in `user_answer` as a string.

```python
print()
```

This prints an additional blank line to help maintain the expected output formatting.

### 5. Storing the Result

```python
results.append(question.check(user_answer))
```

The `check()` method evaluates the user's answer and returns `True` or `False`.

The `append()` method adds that Boolean result to the `results` list.

For example, if three questions produce the results `True`, `False`, and `True`, the list becomes:

```python
results = [True, False, True]
```

### 6. Printing the Final Results

```python
return self.print_results(results)
```

After all questions have been answered, the `start()` method passes the completed results list to `print_results()`.

This allows the quiz to display the overall score and the outcome of each question.

### 7. Calculating the Score

```python
score = sum(results)
total = len(results)
```

The built-in `sum()` function adds the Boolean values in the list. In Python, `True` behaves like `1` and `False` behaves like `0`.

For example:

```python
results = [True, False, True]

score = sum(results)  # 2
total = len(results)  # 3
```

Therefore, the score is `2/3`.

### 8. Displaying the Score

```python
print(f"Your score is {score}/{total}\n")
```

The f-string inserts the calculated score and total number of questions into the output.

Example:

```text
Your score is 2/3
```

The `\n` adds a blank line after the score, separating it from the individual question results.

### 9. Displaying Pass or Fail

```python
for idx, passed in enumerate(results, start=1):
    status = "Pass" if passed else "Fail"
    print(f"[{idx}] {status}")
```

The `enumerate()` function iterates through the results while providing a question number.

- `start=1` makes the numbering begin at `1`.
- The conditional expression assigns `"Pass"` when `passed` is `True`.
- Otherwise, it assigns `"Fail"`.

For example, given:

```python
results = [True, False, True]
```

The output is:

```text
[1] Pass
[2] Fail
[3] Pass
```

## Example of the Complete Output

If a quiz contains three questions and the user's answers produce `[True, False, True]`, the results section will look like this:

```text
Your score is 2/3

[1] Pass
[2] Fail
[3] Pass
```

## Key Takeaway

This solution connects the quiz's main workflow with its result-reporting functionality.

- `start()` displays questions, collects answers, and records their results.
- `results.append()` builds a list of Boolean outcomes.
- `sum(results)` calculates the number of correct answers because `True` counts as `1` and `False` as `0`.
- `enumerate(results, start=1)` numbers each result from one.
- A conditional expression selects either `"Pass"` or `"Fail"`.

Together, these methods provide a complete quiz flow, from presenting questions to displaying the final score.
