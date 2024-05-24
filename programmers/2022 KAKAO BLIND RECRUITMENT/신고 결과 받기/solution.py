def solution(id_list, report, k):
    id_index = {}
    for i in range(len(id_list)):
        id_index[id_list[i]] = i

    reported = {}
    for rpt in report:
        [user, reported_user] = rpt.split(' ')

        if reported_user not in reported:
            reported[reported_user] = set()

        reported[reported_user].add(user)

    answer = [0 for _ in range(len(id_list))]
    for reported_user in reported:
        users = reported[reported_user]
        if len(users) < k:
            continue

        for user in users:
            answer[id_index[user]] += 1

    return answer
