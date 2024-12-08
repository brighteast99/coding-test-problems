def solution(people, limit):
    people.sort(reverse=True)
    p1, p2 = 0, len(people) - 1
    answer = 0
    while p1 <= p2:
        if people[p1] + people[p2] <= limit:
            p2 -= 1

        p1 += 1
        answer += 1

    return answer
