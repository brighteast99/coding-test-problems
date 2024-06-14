def solution(name):
    changes = 0
    targets = []
    for (idx, char) in enumerate(name):
        if char == 'A':
            continue

        targets.append(idx)
        changes += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    min_moves = len(name) - 1
    stack = [(targets[:], 0, 0)]
    while stack:
        targets_left, idx, moves = stack.pop()
        if not targets_left:
            min_moves = min(min_moves, moves)
            continue

        left, right = targets_left[-1], targets_left[0]
        stack += [(targets_left[1:], right, moves + (right - idx) % len(name)),
                  (targets_left[:-1], left, moves + (idx - left) % len(name))]

    return changes + min_moves
