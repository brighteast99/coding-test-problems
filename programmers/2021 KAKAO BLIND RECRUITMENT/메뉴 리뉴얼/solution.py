import itertools
from collections import Counter


def solution(orders, course):
    combinations = [[] for _ in range(len(course))]
    for order in orders:
        order = ''.join(sorted(list(order)))

        for i in range(len(course)):
            combinations[i].extend(map(lambda tpl: ''.join(tpl), itertools.combinations(order, course[i])))

    answer = []
    for combination in combinations:
        if len(combination) == 0:
            continue

        combination = Counter(combination)
        max_val = max(combination.values())
        if max_val < 2:
            continue

        answer.extend([key for key in combination.keys() if combination[key] == max_val])

    return sorted(answer)
