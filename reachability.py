def reachability(graph, node, seen=None):
    seen = seen or []
    seen.append(node)
    reached = set(node)
    adjacent = graph.get(node)

    if adjacent:
        reached.update(adjacent)
        for subnode in adjacent:
            if subnode not in seen:
                reached.update(reachability(graph, subnode, seen))
    final_result = list(reached)
    return final_result
