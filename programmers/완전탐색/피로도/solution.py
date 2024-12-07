import itertools


def solution(k, dungeons):
    answer = -1

    for sequence in itertools.permutations(dungeons):
        n = 0
        cur_k = k
        for [min_k, cost] in sequence:
            if cur_k > min_k:
                cur_k -= cost
                n += 1
        print(sequence, n)
        answer = max(answer, n)

    return answer
