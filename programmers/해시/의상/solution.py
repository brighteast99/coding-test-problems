def solution(clothes):
    categories = dict()
    for _, category in clothes:
        try:
            categories[category] += 1
        except KeyError:
            categories[category] = 1

    ans = 1
    for category in categories:
        ans *= categories[category] + 1

    return ans - 1
