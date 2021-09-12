import os
from random import randint


def generate_random_arena(num_nodes, max_priority, max_successors, folder, pedix):
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

    base_path = os.path.join("../assets/random_arenas", folder)
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    file = open(os.path.join(base_path, "arena_") + str(num_nodes)
                + "_" + str(max_priority) + "_" + str(max_successors) + "_" + str(pedix) + ".txt", "w")

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


# for p in [2, 3, 5]:
# for p in [10, 50, 100]:
#     for n in range(200, 2200, 200):
#         folder_name = "priority" + str(p) + "/nodes" + str(n)
#         for i in range(10):
#             generate_random_arena(n, p, n, folder_name, i)
#     print("Priority ", p, " DONE\n")

# for n in range(200, 2200, 200):
#     folder_name = "priorityN" + "/nodes" + str(n)
#     for i in range(10):
#         generate_random_arena(n, n, n, folder_name, i)
# print("Priority N DONE\n")
