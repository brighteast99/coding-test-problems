def solution(tickets):
    tickets_dict = dict()

    for idx, [frm, to] in enumerate(tickets):
        try:
            tickets_dict[frm].append((to, idx))
            tickets_dict[frm].sort(reverse=True)
        except KeyError:
            tickets_dict[frm] = [(to, idx)]

    stack = []
    for to, idx in tickets_dict["ICN"]:
        stack.append((["ICN", to], {idx}))

    while len(stack):
        route, used = stack.pop()

        if len(route) == len(tickets) + 1:
            return route

        if route[-1] not in tickets_dict or len(tickets_dict[route[-1]]) == 0:
            continue

        for dest, idx in tickets_dict[route[-1]]:
            if idx in used:
                continue
            stack.append(([*route, dest], {*used, idx}))
