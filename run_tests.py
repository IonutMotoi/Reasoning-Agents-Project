import os

from arena.load_arena import load_arena
from solvers.reachability import reachability_solver
from solvers.safety import safety_solver
from solvers.buchi import buchi_solver
from solvers.cobuchi import cobuchi_solver
from tools.output import print_results, save_results

# Reachability
name_arena = "arenawiki.txt"
arena_wiki = load_arena(os.path.join("assets", name_arena))
R = [4, 5]
(win0, strat0), (win1, strat1) = reachability_solver(arena_wiki, R)
save_results("Reachability", name_arena, win0, win1, strat0, strat1)

def reachability_test():
    arena = load_arena("assets/arena0.txt")
    R = [4, 5]
    (win0, strat0), (win1, strat1) = reachability_solver(arena_wiki, R)





