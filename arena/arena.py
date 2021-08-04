from collections import defaultdict


class Arena:
    def __init__(self):
        self.nodes = defaultdict(int)  # 0 or 1
        self.successors = defaultdict(list)
        self.predecessors = defaultdict(list)
        self.importance = defaultdict(lambda: -1)

    def add_node(self, node, player):
        """
        Adds a node to the arena with the relative player
        :param node:
        :param player:
        :return:
        """
        self.nodes[node] = player

    def remove_node(self, node):
        """
        Adds a node to the arena with the relative player
        :param node:
        :return:
        """
        del self.nodes[node]

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

    def set_player(self, node, player):
        """
        Assigns the node to a player
        :param node: id of a node
        :param player: the player to which the node will be assigned
        :return:
        """
        self.nodes[node] = player

    def set_importance(self, node, importance):
        """
        Adds the importance of a node
        :param node: The node to which the importance is assigned
        :param importance: The value of the importance
        :return:
        """
        self.importance[node] = importance

    def get_importance(self, node):
        """
        :param node: id of a node
        :return: the importance of the given node
        """
        return self.importance[node]

    def get_sub_arena(self, nodes):
        """
        Creates a sub-arena from the current game. The sub-game will contain all nodes in the provided set.
        :param nodes: the list of nodes that the sub-arena will contain.
        :return: a sub-arena.
        """
        sub_arena = self.__class__()
        for node in nodes:
            sub_arena.nodes[node] = self.nodes[node]
            sub_arena.importance[node] = self.importance[node]
        for node in sub_arena.nodes:
            for successor in self.successors[node]:
                if successor in sub_arena.nodes:
                    sub_arena.successors[node].append(successor)
                    sub_arena.predecessors[successor].append(node)
        return sub_arena

    def get_max_importance(self):
        return max(self.importance.values())

    def __str__(self):
        arena_str = ""
        for node in self.nodes:
            arena_str += str(node) + " Player" + str(self.nodes[node]) + "\n" + str(node) + " -> "
            for successor in self.successors[node]:
                arena_str += str(successor) + ", "
            arena_str += "\n"
        return arena_str
