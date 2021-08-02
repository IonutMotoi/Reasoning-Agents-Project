from collections import defaultdict


def parity_solver(arena):
    nodes = arena.get_nodes()
    for node in nodes:
        print(node, arena.get_importance(node))
