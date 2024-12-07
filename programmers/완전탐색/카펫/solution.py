def solution(brown, yellow):
    sum = (brown + 4) // 2
    mul = brown + yellow

    for w in reversed(range(3, mul + 1)):
        if mul % w != 0:
            continue

        h = mul // w
        if w + h != sum:
            continue

        return [w, h]
