from reachability import reachability_solver


def safety_solver(arena, s):

    nodes = arena.get_nodes()

    print("nodes", nodes)

    dual_set = [x for x in nodes if x not in s]

    (region_0, strategy_0), (region_1, strategy_1) = reachability_solver(arena, dual_set)

    return (region_1, strategy_1), (region_0, strategy_0)
