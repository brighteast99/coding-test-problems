def solution(cap, n, deliveries, pickups):
    deliveries_left = deliveries[:]
    pickups_left = pickups[:]

    answer = 0
    while deliveries_left or pickups_left:
        while deliveries_left and not deliveries_left[-1]:
            deliveries_left.pop()
        while pickups_left and not pickups_left[-1]:
            pickups_left.pop()

        answer += max(len(deliveries_left), len(pickups_left)) * 2

        deliver_cap = cap
        while deliver_cap > 0:
            if not deliveries_left:
                break
            if deliveries_left[-1] > deliver_cap:
                deliveries_left[-1] -= deliver_cap
                break
            deliver_cap -= deliveries_left.pop()

        pickup_cap = cap
        while pickup_cap > 0:
            if not pickups_left:
                break
            if pickups_left[-1] > pickup_cap:
                pickups_left[-1] -= pickup_cap
                break
            pickup_cap -= pickups_left.pop()

    return answer
