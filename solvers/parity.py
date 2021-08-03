from collections import defaultdict
from solvers.buchi import attractor


def parity_solver(arena):

    # print("nodes in arena", nodes)
    # if nodes:
    #     pass
    # else:
    #     return None, None
    # importance = defaultdict(lambda:-1)
    # for node in nodes:
    #     importance[node] = arena.get_importance(node)  # create dict with nodes and priority
    # p = max(importance.values())  # maximum value of priority

    # print("importance with nodes", dict(importance))
    # print("maximum importance", p)

    # if p == 0:
    #     win_player0 = nodes
    #     win_player1 = []
    #     return win_player0, win_player1
    # else:
    #     u = []
    #     # get nodes in arena with max priority p
    #     for nodes in importance:
    #         if importance[nodes] == p:
    #             u.append(nodes)
    #     # let i the player associated with the maximum priority
    #     i = p % 2
    #     attractor_i = attractor(arena, u)
    #     print("attractor region player i", attractor_i)
    #
    #     nodes = arena.get_nodes()  # need to recompute since it's modified, then let's see
    #     new_set = [x for x in nodes if x not in attractor_i]
    #     print("new set of nodes in arena", new_set)
    #     for node in attractor_i:
    #         arena.remove_node(node)
    #     # print("New graph, with nodes from attractor region removed", arena)
    #     win_player0, win_player1 = parity_solver(arena)

    # V
    nodes = arena.get_nodes()
    print("NODES:", nodes)
    # Minimal color occurring in the game
    d = arena.get_min_importance()

    # Parity of the minimal color occurring in the game
    i = d % 2

    # Set D of states colored with d
    set_d = []
    for node in nodes:
        if arena.get_importance(node) == d:
            set_d.append(node)
    print("Set D =", set_d)

    # Attractor A of the region D
    attractor_i = attractor(arena, set_d)
    print("Attractor region player", i, ":", attractor_i)

    # V \ A
    attractor_i_prime = [x for x in nodes if x not in attractor_i]
    print("A_prime =", attractor_i_prime)

    # Case 1 -> A = V
    if not attractor_i_prime:
        win_player0 = nodes
        win_player1 = []
        return win_player0, win_player1
    # Case 2 -> A != V
    else:
        sub_arena = arena.get_sub_arena(attractor_i_prime)
        win_player0, win_player1 = parity_solver(sub_arena)

        # Subcase 1 -> win_player1 is empty set
        if not win_player1:
            win_player0 = nodes
            win_player1 = []
            return win_player0, win_player1

        # Subcase 2 -> win_player1 not empty set
        else:
            attractor_b = attractor(win_player1)
            sub_arena_2 = sub_arena.get_sub_arena(attractor_b)
            win_player0_b, win_player1_b = parity_solver(sub_arena_2)
            win_player1.append(win_player1_b)
            return win_player0, win_player1

