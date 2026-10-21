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
        print(f'[?] {self.question} (yes/no)\n')

    def check(self, answer):
        result = True if (answer == 'yes' and 
        self.answer == True) or (answer == 'no'
        and self.answer == False) else False
        return result


class OpenQuestion(Question):
    def __init__(self, question: str, answers: list[str]):
        self.question = question
        self.answers = answers

    def print(self):
        print(f"[?] {self.question}\n")

    def check(self, answer: str):
        return answer in self.answers
    

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
        print()

    def check(self, answer: str):
        return int(answer) == self.answer_index + 1


class Quiz():
    def __init__(self, questions: list):
        self.questions = questions
    
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

