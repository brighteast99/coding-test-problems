def solution(bridge_length, weight, truck_weights):
    t = 0
    bridge = [0] * bridge_length
    weight_on_bridge = 0
    while len(truck_weights) > 0:
        t += 1
        weight_on_bridge -= bridge.pop(0)

        if weight_on_bridge + truck_weights[0] <= weight:
            weight_on_bridge += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    return t + bridge_length
