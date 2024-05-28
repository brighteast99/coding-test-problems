# from collections import Counter


def solution(weights):
    answer = 0

    cases = [1, 2/3, 0.5, 0.75]

    counter = {}
    for weight in weights:
        if weight not in counter:
            counter[weight] = 0
        counter[weight] += 1
    # or just counter = Counter(weights)

    keys = list(counter.keys())
    for i in range(len(keys) - 1):
        for j in range(i+1, len(keys)):
            w1, w2 = keys[i], keys[j]

            if w1 > w2:
                w1, w2 = w2, w1

            if w1 / w2 in cases:
                answer += counter[w1] * counter[w2]

    for key in keys:
        if counter[key] > 0:
            answer += counter[key] * (counter[key] - 1) / 2

    return answer
