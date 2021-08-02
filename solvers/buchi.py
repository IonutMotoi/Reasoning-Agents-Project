from collections import defaultdict


def attractor(arena, s):
    attr = s.copy()
    queue = s.copy()

    out = defaultdict(int)
    # Compute the number of outgoing edges for each node in the arena
    for node in arena.get_nodes():
        out[node] = len(arena.get_successors(node))

    # While the target set is not empty
    while queue:
        node = queue.pop()
        for predecessor in arena.get_predecessors(node):
            if predecessor not in attr:
                if arena.get_player(predecessor) == 0:
                    queue.append(predecessor)
                    attr.append(predecessor)
                elif arena.get_player(predecessor) == 1:
                    out[predecessor] -= 1
                    if out[predecessor] == 0:
                        queue.append(predecessor)
                        attr.append(predecessor)

    return attr


def controlled_predecessor_player1(arena, r):
    c_pre = r.copy()

    out = defaultdict(int)
    # Compute the number of outgoing edges for each node in the arena
    for node in arena.get_nodes():
        out[node] = len(arena.get_successors(node))

    for node in r:
        for predecessor in arena.get_predecessors(node):
            if predecessor not in c_pre:
                if arena.get_player(predecessor) == 1:
                    c_pre.append(predecessor)
                elif arena.get_player(predecessor) == 0:
                    out[predecessor] -= 1
                    if out[predecessor] == 0:
                        c_pre.append(predecessor)

    return c_pre


def buchi_solver(arena, recurrence_set):
    pre_win_player1 = [-1]
    win_player1 = []
    while pre_win_player1 != win_player1:
        pre_win_player1 = win_player1[:]
        attr_player0 = attractor(arena, recurrence_set)
        win_player1 = [x for x in arena.get_nodes() if x not in attr_player0]

        c_pre_player1 = controlled_predecessor_player1(arena, win_player1)
        recurrence_set = [x for x in recurrence_set if x not in c_pre_player1]

    win_player0 = [x for x in arena.get_nodes() if x not in win_player1]

    return win_player0, win_player1
