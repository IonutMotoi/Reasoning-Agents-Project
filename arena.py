from collections import defaultdict


class Arena:
    def __init__(self):
        self.nodes = defaultdict(int)  # 0 or 1
        self.successors = defaultdict(list)
        self.predecessors = defaultdict(list)

    def add_node(self, node, player):
        """
        Adds a node to the arena with the relative player
        :param node:
        :param player:
        :return:
        """
        self.nodes[node] = player

    def add_successor(self, node, successor):
        """
        Adds a successor to the successors list of the given node
        :param node:
        :param successor:
        :return:
        """
        self.successors[node].append(successor)

    def add_predecessor(self, node, predecessor):
        """
        Adds a predecessor to the predecessors list of the given node
        :param node:
        :param predecessor:
        :return:
        """
        self.predecessors[node].append(predecessor)

    def get_nodes(self):
        """
        :return: the list of all the nodes in the arena
        """
        return self.nodes.keys()

    def get_successors(self, node):
        """
        :param node: id of a node
        :return: list of the successors of the given node
        """
        return self.successors[node]

    def get_predecessors(self, node):
        """
        :param node: id of a node
        :return: list of the predecessors of the given node
        """
        return self.predecessors[node]

    def get_player(self, node):
        """
        :param node: id of a node
        :return: the player to which the node belongs
        """
        return self.nodes[node]

    def __str__(self):
        arena_str = ""
        for node in self.nodes:
            arena_str += str(node) + " Player" + str(self.nodes[node]) + "\n" + str(node) + " -> "
            for successor in self.successors[node]:
                arena_str += str(successor) + ", "
            arena_str += "\n"
        return arena_str
