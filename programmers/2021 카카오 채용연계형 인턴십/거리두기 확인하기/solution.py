from itertools import combinations


def isdistancing(place):
    PERSON = 'P'
    PARTITION = 'X'

    people = []

    for row in range(5):
        for col in range(5):
            if place[row][col] == PERSON:
                people.append((row, col))

    violated = False
    for ((y1, x1), (y2, x2)) in combinations(people, 2):
        distance = abs(y1 - y2) + abs(x1 - x2)
        if distance > 2:
            continue
        if distance == 1:
            violated = True
            break
        if y1 == y2:
            if place[y1][(x1 + x2) // 2] != PARTITION:
                violated = True
                break
            else:
                continue
        if x1 == x2:
            if place[(y1 + y2) // 2][x1] != PARTITION:
                violated = True
                break
            else:
                continue
        if place[y1][x2] != PARTITION or place[y2][x1] != PARTITION:
            violated = True
            break

    return not violated


def solution(places):
    return list(map(lambda place: int(isdistancing(place)), places))
