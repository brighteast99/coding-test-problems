import sys

END = 32

SCORE = {id: id * 2 for id in range(1, 21)}
SCORE[21], SCORE[22], SCORE[23] = 13, 16, 19
SCORE[24], SCORE[25] = 22, 24
SCORE[26], SCORE[27], SCORE[28] = 28, 27, 26
SCORE[29], SCORE[30], SCORE[31] = 25, 30, 35
SCORE[END] = 0  # End

BOARD = {id: [id + 1] for id in range(0, 20)}
BOARD[5].append(21)
BOARD[21], BOARD[22], BOARD[23] = [22], [23], [29]
BOARD[10].append(24)
BOARD[24], BOARD[25] = [25], [29]
BOARD[15].append(26)
BOARD[26], BOARD[27], BOARD[28] = [27], [28], [29]
BOARD[29], BOARD[30], BOARD[31] = [30], [31], [20]
BOARD[20] = [END]


def dfs(pieces, target, dices, score=0):
    if len(dices) == 0:
        return score

    move = dices[0]
    if pieces[target] in [5, 10, 15]:
        pieces[target] = BOARD[pieces[target]][1]
        move -= 1
    while move > 0:
        pieces[target] = BOARD[pieces[target]][0]
        move -= 1
        if pieces[target] == END:
            break

    for i, piece in enumerate(pieces):
        if i == target:
            continue
        if piece == pieces[target]:
            return score

    score += SCORE[pieces[target]]
    if pieces[target] == END:
        pieces.pop(target)

    max_score = score
    for i in range(len(pieces)):
        max_score = max(max_score, dfs([*pieces], i, dices[1:], score))

    return max_score


dices = list(map(int, sys.stdin.readline().split()))
print(dfs([0, 0, 0, 0], 0, dices))
