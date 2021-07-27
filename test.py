from reachability import reachability

# Example reachability
graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

print(reachability(graph, 'a'))
# >>> ['a', 'c', 'd', 'b']

print(reachability(graph, 'd'))
# >>> ['d', 'a', 'c', 'b']

print(reachability(graph, 'e'))
# >>> ['e', 'a', 'c', 'd', 'b']