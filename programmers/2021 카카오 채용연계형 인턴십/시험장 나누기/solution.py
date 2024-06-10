def solution(k, num, links):
    is_child = [False] * len(num)

    for [left, right] in links:
        if left != -1:
            is_child[left] = True
        if right != -1:
            is_child[right] = True
    root = is_child.index(False)

    temp = [root]
    post_order = []
    while len(temp) > 0:
        top = temp.pop()
        if top != -1:
            post_order.append(top)
            temp.extend(links[top])
    else:
        post_order.reverse()

    left, right = max(num), sum(num)
    while left <= right:
        size_limit = (left + right) // 2
        groups = 1
        merged_num = num[:]
        for cur in post_order:
            if groups > k:
                break

            group_size = merged_num[cur]
            [left_node, right_node] = links[cur]
            left_size = merged_num[left_node] if left_node != -1 else 0
            right_size = merged_num[right_node] if right_node != -1 else 0

            if group_size + left_size + right_size <= size_limit:
                merged_num[cur] = group_size + left_size + right_size
            elif group_size + min(left_size, right_size) > size_limit:
                groups += 2
            else:
                merged_num[cur] = group_size + min(left_size, right_size)
                groups += 1

        if groups <= k:
            right = size_limit - 1
        else:
            left = size_limit + 1

    return left
