from heapq import heappush, heappop

def solution(n, k, enemy):
    enemies_to_skip = []

    total_enemies = 0
    skipped_enemies = 0
    for (round, num_enemy) in enumerate(enemy):
        total_enemies += num_enemy

        if len(enemies_to_skip) < k or num_enemy > enemies_to_skip[0]:
            heappush(enemies_to_skip, num_enemy)
            skipped_enemies += num_enemy

            if len(enemies_to_skip) > k:
                skipped_enemies -= heappop(enemies_to_skip)

        if total_enemies - skipped_enemies > n:
            return round

    return len(enemy)
