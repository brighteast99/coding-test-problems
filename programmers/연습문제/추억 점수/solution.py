from functools import reduce


def solution(name, yearning, photo):
    scores_by_names = {}

    for i in range(len(name)):
        scores_by_names[name[i]] = yearning[i]

    return list(map(lambda names: reduce(lambda acc, cur: acc + (scores_by_names[cur] if cur in scores_by_names else 0), names, 0), photo))