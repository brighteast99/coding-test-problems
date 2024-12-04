import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    n_mixed = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + 2 * heapq.heappop(scoville))
        n_mixed += 1

    return n_mixed
