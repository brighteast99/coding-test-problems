def solution(board, h, w):
    dx = [0, 0, -1, 1]
    dy = [-1, +1, 0, 0]

    color = board[h][w]
    size = len(board)
    answer = 0
    for i in range(4):
        h_check = h + dy[i]
        w_check = w + dx[i]
        if w_check < 0 or w_check >= size or h_check < 0 or h_check >= size:
            continue

        if board[h_check][w_check] == color:
            answer += 1

    return answer
