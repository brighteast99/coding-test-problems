def solution(participant: list, completion: list):
    s = {participant.pop()}

    for p, c in zip(participant, completion):
        if p in s:
            s.remove(p)
        else:
            s.add(p)

        if c in s:
            s.remove(c)
        else:
            s.add(c)

    return s.pop()
