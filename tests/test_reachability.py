import unittest
from reachability import reachability


class TestReachability(unittest.TestCase):

    def test_reachability1(self):
        graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}
        result = reachability(graph, 'a')
        self.assertCountEqual(result, ['a', 'b', 'c', 'd'])

    def test_reachability2(self):
        graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}
        result = reachability(graph, 'd')
        self.assertCountEqual(result, ['a', 'b', 'c', 'd'])

    def test_reachability3(self):
        graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}
        result = reachability(graph, 'e')
        self.assertCountEqual(result, ['a', 'b', 'c', 'd', 'e'])


if __name__ == '__main__':
    unittest.main()
