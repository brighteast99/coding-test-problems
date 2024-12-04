from itertools import permutations
from operator import add, sub, mul
from re import split


def solution(expression):
    answer = 0

    numbers = list(map(int, split('[\+\-\*]', expression)))
    operators = [op for op in expression if op in '+-*']
    for priority in permutations('+-*', 3):
        def calc(numbers, operators, priority):
            operation_func = {
                '+': add,
                '-': sub,
                '*': mul
            }
            for operator in priority:
                while operator in operators:
                    idx = operators.index(operator)
                    operators.pop(idx)
                    operand1, operand2 = numbers[idx], numbers.pop(idx + 1)
                    numbers[idx] = operation_func[operator](operand1, operand2) if operator in operation_func else 0

            return abs(numbers[0])
        answer = max(answer, calc(numbers[:], operators[:], priority))

    return answer