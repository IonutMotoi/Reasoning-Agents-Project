from collections import defaultdict, deque

def reachability_solver(arena, R):
    """
    Reachability solver
    :param arena:
    :param R: reachability set
    :return: two tuples -> winning region and strategy for both players
    """
    out = defaultdict(int)
    # Compute the number of outgoing edges for each node in the arena
    for node in arena.get_nodes():
        out[node] = len(arena.get_successors(node))

    queue = deque()  # Initialize double ended queue

    # Winning regions for both players
    regions = defaultdict(lambda: -1)
    region_0 = []
    region_1 = []

    # Winning strategies for both players
    strategy_0 = defaultdict(lambda: -1)
    strategy_1 = defaultdict(lambda: -1)

    # For each node in the reachability set
    for node in R:
        queue.append(node)  # Add node at the end fo the queue
        regions[node] = 0  # Node winning for player 0
        region_0.append(node)

        # Can be assigned arbitrarily
        if arena.get_player(node) == 0:
            strategy_0[node] = arena.get_successors(node)[0]
        else:
            strategy_1[node] = arena.get_successors(node)[0]

    # While queue not empty
    while queue:
        node = queue.popleft()  # Pop node from left side (FIFO)
        for predecessor in arena.get_predecessors(node):
            if regions[predecessor] == -1:  # If -1, doesn't belong to a winning region yet
                if arena.get_player(predecessor) == 0:
                    queue.append(predecessor)
                    regions[predecessor] = 0
                    region_0.append(predecessor)
                    strategy_0[predecessor] = node

                elif arena.get_player(predecessor) == 1:
                    out[predecessor] -= 1
                    if out[predecessor] == 0:
                        # Player 1 only has successors from which player 0 can enforce a win
                        queue.append(predecessor)
                        regions[predecessor] = 0
                        region_0.append(predecessor)
                        strategy_1[predecessor] = node  # can be assigned arbitrarily

    for node in arena.get_nodes():
        if regions[node] != 0:
            regions[node] = 1
            region_1.append(node)
            if arena.get_player(node) == 1:
                for successor in arena.get_successors(node):
                    if regions[successor] != 0:
                        strategy_1[node] = successor

    return (region_0, strategy_0), (region_1, strategy_1)
