from arena import Arena
from load_arena import load_arena
from reachability import reachability_solver
from safety import safety_solver

arena = load_arena("example1.txt")

print(arena)

# (win0, strat0), (win1, strat1) = reachability_solver(arena, [4, 5])
# print("Reachability results:")
# print(win0)
# print(strat0)
# print(win1)
# print(strat1)

(winS0, stratS0), (winS1, stratS1) = safety_solver(arena, [1, 2, 3, 4, 5, 7, 8])
print("Safety results:")
print(winS0)
print(stratS0)
print(winS1)
print(stratS1)
