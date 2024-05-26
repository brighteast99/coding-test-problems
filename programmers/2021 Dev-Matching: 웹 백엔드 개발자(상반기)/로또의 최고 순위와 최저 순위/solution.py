def solution(lottos, win_nums):
    min_hits = len(list(filter(lambda num: num in win_nums, lottos)))
    max_hits = min_hits + lottos.count(0)
    return list(map(lambda hits: min(6, 7 - hits), [max_hits, min_hits]))
