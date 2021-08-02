from arena.load_arena import load_arena
from solvers.buchi import buchi_solver
from solvers.cobuchi import cobuchi_solver

arena = load_arena("./assets/arena1.txt")

# print(arena)
#
# (win0, strat0), (win1, strat1) = reachability_solver(arena, [4, 5])
# print("Reachability results:")
# print(win0)
# print(dict(strat0))
# print(win1)
# print(dict(strat1))
#
# print("")
#
# (winS0, stratS0), (winS1, stratS1) = safety_solver(arena, [1, 2, 3, 4, 5, 7, 8])
# print("Safety results:")
# print(winS0)
# print(dict(stratS0))
# print(winS1)
# print(dict(stratS1))
#
# print("")

F = [4, 6]
# win = buchi_solver(arena, F)
# print(win)

# C = [2, 4, 5, 6, 7, 8]
win0, strat0, win1, strat1 = buchi_solver(arena, F)
print(win0)
print(win1)
print(strat0)
print(strat1)