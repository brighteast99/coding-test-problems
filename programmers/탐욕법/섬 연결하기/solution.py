def solution(n, costs):
    costs.sort(key=lambda con: con[2])
    connected = {0}
    total_cost = 0
    while len(connected) < n:
        for i, [a, b, cost] in enumerate(costs):
            if a in connected and b in connected:
                costs.pop(i)
                break
            if a not in connected and b not in connected:
                continue

            costs.pop(i)
            connected.update({a, b})
            total_cost += cost
            break

    return total_cost
