
def find_intersection(ll1, ll2):
    if len(ll1) > len(ll2):
        longer_node = ll1
        shorter_node = ll2
    else:
        longer_node = ll2
        shorter_node = ll1

    diff = abs(len(ll1) - len(ll2))

    for _ in range(diff):
        longer_node = longer_node.next

    while longer_node and shorter_node:
        if longer_node == shorter_node:
            return longer_node

        longer_node = longer_node.next
        shorter_node = shorter_node.next

    return None
