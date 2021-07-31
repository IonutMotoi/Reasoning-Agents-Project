from reachability import reachability_solver


def safety_solver(arena, s):

    nodes = arena.get_nodes()

    dual_arena = arena
    for node in nodes:
        if arena.get_player(node) == 0:
            dual_arena.set_player(node, 1)
        else:
            dual_arena.set_player(node, 0)

    dual_set = [x for x in nodes if x not in s]

    (region_0, strategy_0), (region_1, strategy_1) = reachability_solver(arena, dual_set)

    return (region_1, strategy_1), (region_0, strategy_0)
