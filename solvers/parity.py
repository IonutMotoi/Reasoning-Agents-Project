from collections import defaultdict
from solvers.buchi import attractor


def parity_solver(arena):
    nodes = arena.get_nodes()
    # print("nodes in arena", nodes)
    # if nodes:
    #     pass
    # else:
    #     return None, None
    importance = defaultdict(lambda:-1)
    for node in nodes:
        importance[node] = arena.get_importance(node)  # create dict with nodes and priority
    p = max(importance.values())  # maximum value of priority
    # print("importance with nodes", dict(importance))
    # print("maximum importance", p)
    if p == 0:
        win_player0 = nodes
        win_player1 = []
        return win_player0, win_player1
    else:
        u = []
        # get nodes in arena with max priority p
        for nodes in importance:
            if importance[nodes] == p:
                u.append(nodes)
        # let i the player associated with the maximum priority
        i = p % 2
        attractor_i = attractor(arena, u)
        print("attractor region player i", attractor_i)

        nodes = arena.get_nodes()  # need to recompute since it's modified, then let's see
        new_set = [x for x in nodes if x not in attractor_i]
        print("new set of nodes in arena", new_set)
        for node in attractor_i:
            arena.remove_node(node)
        # print("New graph, with nodes from attractor region removed", arena)
        win_player0, win_player1 = parity_solver(arena)

