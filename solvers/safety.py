from solvers.reachability import reachability_solver


def safety_solver(arena, safety_set):
    """
    Solver for safety games
    :param arena: The arena of the game
    :param safety_set: Safety set
    :return: two tuples -> winning region and strategy for player 0 and player 1
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
    dual_set = [x for x in nodes if x not in safety_set]

    # Swap the winning regions and strategies
    region_1, strategy_1, region_0, strategy_0,  = reachability_solver(arena, dual_set)

    return region_0, strategy_0, region_1, strategy_1
