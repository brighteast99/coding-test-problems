def solution(p):
    if len(p) == 0:
        return p

    paren_balance = 0
    len_u = len(p)
    correct_u = True
    for i in range(len(p)):
        paren_balance += 1 if p[i] == '(' else -1

        if paren_balance < 0:
            correct_u = False

        if paren_balance == 0:
            len_u = i + 1
            break

    u, v = p[:len_u], p[len_u:]

    if correct_u:
        return u + solution(v)

    return '(' + solution(v) + ')' +"".join(["(" if paren == ")" else ")" for paren in u[1:-1]])
