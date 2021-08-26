from collections import defaultdict


def attractor(arena, s, i=0):
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
                if arena.get_player(predecessor) == i:
                    queue.append(predecessor)
                    attr.append(predecessor)
                elif arena.get_player(predecessor) != i:
                    out[predecessor] -= 1
                    if out[predecessor] == 0:
                        queue.append(predecessor)
                        attr.append(predecessor)

    return attr


def attractor_with_strategy(arena, s, i=0):
    attr = s.copy()
    queue = s.copy()

    strat0 = defaultdict(lambda: -1)
    strat1 = defaultdict(lambda: -1)

    out = defaultdict(int)
    # Compute the number of outgoing edges for each node in the arena
    for node in arena.get_nodes():
        out[node] = len(arena.get_successors(node))
        if node in s:
            if arena.get_player(node) == i:
                strat0[node] = arena.get_successors(node)[0]
            else:
                strat1[node] = arena.get_successors(node)[0]

    # While the target set is not empty
    while queue:
        node = queue.pop()
        for predecessor in arena.get_predecessors(node):
            if predecessor not in attr:
                if arena.get_player(predecessor) == i:
                    queue.append(predecessor)
                    attr.append(predecessor)
                    strat0[predecessor] = node
                elif arena.get_player(predecessor) != i:
                    out[predecessor] -= 1
                    if out[predecessor] == 0:
                        queue.append(predecessor)
                        attr.append(predecessor)
                        strat1[predecessor] = node
            elif arena.get_player(predecessor) != i:
                # in attraction region of player 0
                # strategy of player 1 can be arbitrary
                strat1[predecessor] = node

    return attr, strat0, strat1


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

    _, strategy_player0, strategy_player1 = attractor_with_strategy(arena, recurrence_set)

    for node in attr_player0:
        if arena.get_player(node) == 0:
            if node in recurrence_set:  # node in F^m
                successors = arena.get_successors(node)
                for successor in successors:
                    if successor in attr_player0:
                        strategy_player0[node] = successor
                        break
            else:  # node in Attr_0(F^m) \ F^m
                pass

    for node in arena.get_nodes():
        if arena.get_player(node) == 0:
            if strategy_player0[node] == -1:
                # can be arbitrary
                strategy_player0[node] = arena.get_successors(node)[0]
        elif arena.get_player(node) == 1:
            for successor in arena.get_successors(node):
                if successor in win_player1:
                    strategy_player1[node] = successor

    return win_player0, strategy_player0, win_player1, strategy_player1
