def solution(info, query):
    languages_idx = {"-": 0, "cpp": 1, "java": 2, "python": 3}
    jobs_idx = {"-": 0, "backend": 1, "frontend": 2}
    careers_idx = {"-": 0, "junior": 1, "senior": 2}
    foods_idx = {"-": 0, "chicken": 1, "pizza": 2}
    groups = [[[[[] for ____ in range(3)] for ___ in range(
        3)] for __ in range(3)] for _ in range(4)]
    answer = []

    for applicant in info:
        [language, job, career, food, score] = applicant.split(' ')
        score = int(score)
        for l in ["-", language]:
            for j in ["-", job]:
                for c in ["-", career]:
                    for f in ["-", food]:
                        groups[languages_idx[l]][jobs_idx[j]
                                                 ][careers_idx[c]][foods_idx[f]].append(score)

    for language in languages_idx.values():
        for job in jobs_idx.values():
            for career in careers_idx.values():
                for food in foods_idx.values():
                    groups[language][job][career][food].sort(reverse=True)

    for q in query:
        conditions = q.split(' ')
        required_score = int(conditions.pop())
        [language, job, career, food] = [
            condition for condition in conditions if condition != 'and']

        def binary_search(arr, val, start, end):
            if start > end:
                return end

            mid = (start + end) // 2
            if arr[mid] >= val:
                return binary_search(arr, val, mid + 1, end)
            if arr[mid] < val:
                return binary_search(arr, val, start, mid - 1)

        group = groups[languages_idx[language]][jobs_idx[job]
                                                ][careers_idx[career]][foods_idx[food]]
        answer.append(binary_search(
            group, required_score, 0, len(group) - 1) + 1)

    return answer
