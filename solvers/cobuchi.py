from solvers.buchi import buchi_solver


def cobuchi_solver(arena, persistence_set):
    """
        Solver for safety games
        :param arena: The arena of the game
        :param persistence_set: Persistence set
        :return: two tuples -> winning region for player 0 and player 1
        """
    nodes = arena.get_nodes()

    # Solve safety game by turning it into a reachability game (duality)
    dual_arena = arena
    for node in nodes:
        # Swap the vertices of the players
        if arena.get_player(node) == 0:
            dual_arena.set_player(node, 1)
        else:
            dual_arena.set_player(node, 0)

    # Get the dual of the safety set (V\S)
    dual_set = [x for x in nodes if x not in persistence_set]

    # Swap the winning regions and strategies
    region_1, region_0 = buchi_solver(arena, dual_set)

    return region_0, region_1
