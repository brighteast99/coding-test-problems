class Num:
    def __init__(self, val):
        self.val = val

    def __comp__(self, other):
        return f"{self.val}{other.val}" < f"{other.val}{self.val}"


def solution(numbers):
    numbers = list(map(Num, numbers))
    numbers.sort()
    return "".join(numbers)
