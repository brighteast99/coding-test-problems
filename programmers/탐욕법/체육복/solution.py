def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()

    reserve = set(reserve)
    self_reserve = reserve.intersection(lost)
    answer += len(self_reserve)
    lost = [l for l in lost if l not in self_reserve]
    reserve.difference_update(self_reserve)

    for l in lost:
        if l - 1 in reserve:
            answer += 1
            reserve.remove(l - 1)
            continue
        if l + 1 in reserve:
            answer += 1
            reserve.remove(l + 1)

    return answer
