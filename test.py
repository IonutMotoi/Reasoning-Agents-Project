from arena import Arena
from load_arena import load_arena
from reachability import reachability_solver

arena = load_arena("example1.txt")

print(arena)

(win0, strat0), (win1, strat1) = reachability_solver(arena, [4, 5])

print(win0)
print(strat0)
print(win1)
print(strat1)