from itertools import combinations

def solution(relation):
    columns = len(relation[0])
    keys = []
    for i in range(1, columns + 1):
        keys.extend(list(map(set, combinations(range(columns), i))))

    candidate_keys = []
    for key in keys:
        is_minimal = True
        for candidate_key in candidate_keys:
            if candidate_key.issubset(key):
                is_minimal = False
        if not is_minimal:
            continue

        projected = [tuple(relation[row][col] for col in key) for row in range(len(relation))]
        if len(projected) != len(set(projected)):
            continue

        candidate_keys.append(key)

    return len(candidate_keys)
