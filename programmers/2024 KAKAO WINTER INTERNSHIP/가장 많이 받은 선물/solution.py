def solution(friends, gifts):
    name_index = {}
    for i, friend in enumerate(friends):
        name_index[friend] = i

    scores = [0 for _ in friends]
    gift_log = [[0 for _ in friends] for _ in friends]

    for gift in gifts:
        sender, receiver = map(lambda name: name_index[name], gift.split(" "))
        scores[sender] += 1
        scores[receiver] -= 1
        gift_log [sender][receiver] += 1

    gift = [0 for _ in friends]
    for friend1 in range(len(friends)):
        for friend2 in range(friend1 + 1, len(friends)):
            print(friends[friend1], friends[friend2])
            if gift_log[friend1][friend2] > gift_log[friend2][friend1]:
                gift[friend1] += 1
            elif gift_log[friend1][friend2] < gift_log[friend2][friend1]:
                gift[friend2] += 1
            else:
                if (scores[friend1] > scores[friend2]):
                    gift[friend1] += 1
                elif (scores[friend1] < scores[friend2]):
                    gift[friend2] += 1

    return max(gift)