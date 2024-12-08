def solution(n, wires):
    answer = n
    for cut in range(len(wires)):
        new_wires = set((wire[0], wire[1]) for i, wire in enumerate(wires) if i != cut)
        network = set()

        while True:
            for wire in new_wires:
                if len(network) == 0 or wire[0] in network or wire[1] in network:
                    network.add(wire[0])
                    network.add(wire[1])
                    new_wires.remove(wire)
                    break
            else:
                break

        answer = min(answer, abs(n - 2 * len(network)))
    return answer
