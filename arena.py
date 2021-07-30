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

    def __str__(self):
        arena = ""
        for node in self.nodes:
            arena += str(node) + " " + str(self.nodes[node]) + "\n" + str(node) + " -> "
            for successor in self.successors[node]:
                arena += str(successor) + ", "
            arena += "\n"
        return arena
