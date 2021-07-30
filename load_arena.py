from arena import Arena

"""
File used to load the arena, and print out the solution
"""


def load_arena(file):
    with open(file, "r") as f:
        arena = Arena()
        for line in f:
            split_line = line.split(" ")
            node = int(split_line[0])
            if split_line[1] == "0":
                arena.add_node(node, 0)
            else:
                arena.add_node(node, 1)

            for successor in split_line[2].split(","):
                arena.add_successor(node, int(successor))
                arena.add_predecessor(int(successor), node)

    return arena
