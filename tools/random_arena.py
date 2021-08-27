import os
from random import randint


def generate_random_arena(num_nodes, max_priority, max_successors):
    """
    Generates a random arena and exports it to a txt file
    The txt file will have the following format:
        ...
        nodeN player importance successor,successor2,...
        nodeN+1 player importance successor,successor2,...
        ...
    :param num_nodes: The number of nodes that the arena will have
    :param max_priority: The maximum priority that a node can have
    :param max_successors: The maximum number of outgoing edges for each node (min: 1)
    :return:
    """
    assert max_priority >= 0, "max_priority cannot be a negative number"
    assert max_successors > 0, "max_successors must be greater or equal to 1 (valid arena)"

    if not os.path.exists("../assets/random_arenas"):
        os.makedirs("../assets/random_arenas")
    file = open("../assets/random_arenas/ran_arena_" + str(num_nodes)
                + "_" + str(max_priority) + "_" + str(max_successors) + ".txt", "w")

    for node in range(num_nodes):
        # Random player
        player = randint(0, 1)

        # Random priority
        priority = randint(0, max_priority)

        # Random successors
        num_successors = randint(1, max_successors)
        successor_list = []
        for i in range(num_successors):
            successor = randint(0, num_nodes-1)
            if successor not in successor_list:
                successor_list.append(successor)
        successors = [str(element) for element in successor_list]
        successors = ",".join(successors)

        # Format:
        # node player priority successors
        file.write("%d %d %d %s" % (node, player, priority, successors))
        file.write("\n")

    file.close()


# generate_random_arena(10, 10, 10)
# generate_random_arena(100, 100, 10)
# generate_random_arena(1000, 1000, 10)
# generate_random_arena(10000, 10000, 10)
# generate_random_arena(100000, 100000, 10)
# generate_random_arena(1000000, 1000000, 10)
# generate_random_arena(10000000, 10000000, 10)
# generate_random_arena(100000000, 100000000, 10)
