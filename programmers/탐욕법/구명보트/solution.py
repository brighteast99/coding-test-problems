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


# Solution using deque
# from collections import deque


# def solution(people, limit):
#     people.sort(reverse=True)
#     dq = deque(people)
#     answer = 0
#     while len(dq):
#         if len(dq) > 1 and dq[0] + dq[-1] <= limit:
#             dq.pop()

#         dq.popleft()
#         answer += 1

#     return answer
