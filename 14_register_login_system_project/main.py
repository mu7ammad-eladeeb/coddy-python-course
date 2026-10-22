def maintain_set(a_set, number):
    if number in a_set:
        return number * 2

    a_set.add(number)
    return a_set
