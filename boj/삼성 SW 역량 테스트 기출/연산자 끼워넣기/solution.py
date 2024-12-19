import sys


def divide(a, b):
    if a > 0:
        return a // b

    return -((-a) // b)


def find(numbers, operators, comparator, accum):
    left = sum(operators)
    if left == 0:
        return accum

    cases = []
    pls, mns, mul, div = operators

    if pls > 0:
        cases.append(
            find(numbers, [pls - 1, mns, mul, div], comparator, accum + numbers[-left])
        )
    if mns > 0:
        cases.append(
            find(numbers, [pls, mns - 1, mul, div], comparator, accum - numbers[-left])
        )
    if mul > 0:
        cases.append(
            find(numbers, [pls, mns, mul - 1, div], comparator, accum * numbers[-left])
        )
    if div > 0:
        cases.append(
            find(
                numbers,
                [pls, mns, mul, div - 1],
                comparator,
                divide(accum, numbers[-left]),
            )
        )

    return comparator(cases)


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))

print(find(numbers, operators, max, numbers[0]))
print(find(numbers, operators, min, numbers[0]))
