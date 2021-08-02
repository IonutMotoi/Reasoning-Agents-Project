from arena.arena import Arena


def load_arena(file):
    """
    Loads the arena from a txt file that has the following format:
    [node number] [player (0 or 1)] [importance (ignored by this function)] [successors (comma separated)]
    :param file: Path to the txt file describing the arena
    :return: The loaded arena
    """
    with open(file, "r") as f:
        arena = Arena()
        for line in f:
            split_line = line.split(" ")
            node = int(split_line[0])
            if split_line[1] == "0":
                arena.add_node(node, 0)
            else:
                arena.add_node(node, 1)

            for successor in split_line[3].split(","):
                arena.add_successor(node, int(successor))
                arena.add_predecessor(int(successor), node)

    return arena


def load_arena_parity(file):
    """
    Loads the arena for a parity game from a txt file that has the following format:
    [node number] [player (0 or 1)] [importance] [successors (comma separated)]
    :param file: Path to the txt file describing the arena
    :return: The loaded arena
    """
    with open(file, "r") as f:
        arena = Arena()
        for line in f:
            split_line = line.split(" ")
            node = int(split_line[0])
            if split_line[1] == "0":
                arena.add_node(node, 0)
            else:
                arena.add_node(node, 1)

            arena.set_importance(node, int(split_line[2]))

            for successor in split_line[3].split(","):
                arena.add_successor(node, int(successor))
                arena.add_predecessor(int(successor), node)

    return arena
