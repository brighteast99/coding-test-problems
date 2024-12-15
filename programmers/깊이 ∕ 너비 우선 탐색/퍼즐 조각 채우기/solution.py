from collections import deque


def find_piece(board, x, y):
    BOARD_SIZE = len(board)
    x_min, x_max, y_min, y_max = BOARD_SIZE, -1, BOARD_SIZE, -1
    blocks = set()

    dq = deque([(x, y)])
    while len(dq) > 0:
        pos = dq.popleft()

        cur_x, cur_y = pos
        if not (0 <= cur_x < BOARD_SIZE) or not (0 <= cur_y < BOARD_SIZE):
            continue
        if board[cur_y][cur_x] == 0:
            continue
        if pos in blocks:
            continue

        board[cur_y][cur_x] = 0
        x_min, x_max = min(x_min, cur_x), max(x_max, cur_x)
        y_min, y_max = min(y_min, cur_y), max(y_max, cur_y)
        blocks.add((cur_x, cur_y))

        dq.extend(
            (cur_x + dx, cur_y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        )

    return [
        [1 if (x, y) in blocks else 0 for x in range(x_min, x_max + 1)]
        for y in range(y_min, y_max + 1)
    ]


def match(space, piece):
    w_space, h_space = len(space[0]), len(space)
    w_piece, h_piece = len(piece[0]), len(piece)

    if w_space == w_piece and h_space == h_piece and w_space == h_space:
        return (
            all(
                space[y][x] == piece[y][x]
                for x in range(w_space)
                for y in range(h_space)
            )
            or all(
                space[y][x] == piece[w_space - 1 - x][y]
                for x in range(w_space)
                for y in range(h_space)
            )
            or all(
                space[y][x] == piece[x][h_space - 1 - y]
                for x in range(w_space)
                for y in range(h_space)
            )
            or all(
                space[y][x] == piece[h_space - 1 - y][w_space - 1 - x]
                for x in range(w_space)
                for y in range(h_space)
            )
        )
    if w_space == w_piece and h_space == h_piece:
        return all(
            space[y][x] == piece[y][x] for x in range(w_space) for y in range(h_space)
        ) or all(
            space[y][x] == piece[h_space - 1 - y][w_space - 1 - x]
            for x in range(w_space)
            for y in range(h_space)
        )
    if w_space == h_piece and h_space == w_piece:
        return all(
            space[y][x] == piece[w_space - 1 - x][y]
            for x in range(w_space)
            for y in range(h_space)
        ) or all(
            space[y][x] == piece[x][h_space - 1 - y]
            for x in range(w_space)
            for y in range(h_space)
        )
    else:
        return False


def get_size(piece):
    return sum([sum(row) for row in piece])


def solution(game_board, table):
    BOARD_SIZE = len(game_board)
    game_board = [[1 if pos == 0 else 0 for pos in row] for row in game_board]
    spaces, pieces = [], []

    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if game_board[y][x] != 0:
                spaces.append(find_piece(game_board, x, y))
            if table[y][x] != 0:
                pieces.append(find_piece(table, x, y))

    answer = 0
    while len(pieces):
        piece = pieces.pop()
        for i, space in enumerate(spaces):
            if match(space, piece):
                answer += get_size(piece)
                spaces.pop(i)
                break

    return answer
