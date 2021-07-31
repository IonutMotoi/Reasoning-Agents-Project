from collections import defaultdict


def attractor(arena, s):
    attr = s.copy()

    out = defaultdict(int)
    # Compute the number of outgoing edges for each node in the arena
    for node in arena.get_nodes():
        out[node] = len(arena.get_successors(node))

    # While the target set is not empty
    while s:
        node = s.pop()
        for predecessor in arena.get_predecessors(node):
            if predecessor not in attr:
                if arena.get_player(predecessor) == 0:
                    s.append(predecessor)
                    attr.append(predecessor)
                elif arena.get_player(predecessor) == 1:
                    out[predecessor] -= 1
                    if out[predecessor] == 0:
                        s.append(predecessor)
                        attr.append(predecessor)

    return attr


def buchi_solver(arena, recurrence_set):
    attr = attractor(arena, recurrence_set)
    win_1 = [x for x in arena.get_nodes() if x not in attr]
    return win_1
