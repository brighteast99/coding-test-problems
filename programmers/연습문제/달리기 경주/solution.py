def solution(players, callings):
    ranks = {}

    for i in range(len(players)):
        ranks[players[i]] = i

    for calling in callings:
        idx = ranks[calling]
        ranks[calling] -= 1
        ranks[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]

    return players