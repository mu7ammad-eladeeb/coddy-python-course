def maintain_set(numbers, number):
    if number in numbers:
        return number * 2

    numbers.add(number)
    return numbers
