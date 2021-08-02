from arena.load_arena import load_arena
from solvers.reachability import reachability_solver
from solvers.safety import safety_solver
from solvers.buchi import buchi_solver
from solvers.cobuchi import cobuchi_solver
from tools.output import print_results

import argparse

arena = load_arena("assets/arena1.txt")

# Create the parser
my_parser = argparse.ArgumentParser(description='Choose the game to play')

# Add the arguments
my_parser.add_argument('--game', type=str, required=False)

# Execute the parse_args() method
args = my_parser.parse_args()

# print(arena)

# Reachability solver
if args.game == "reachability":
    (win0, strat0), (win1, strat1) = reachability_solver(arena, [4, 5])
    print_results("Reachability", win0, win1, strat0, strat1)

# Safety Solver
elif args.game == "safety":
    (win0, strat0), (win1, strat1) = safety_solver(arena, [1, 2, 3, 4, 5, 7, 8])
    print_results("Safety", win0, win1, strat0, strat1)

# Buchi solver
elif args.game == "buchi":
    F = [4, 6]
    win0, strat0, win1, strat1 = buchi_solver(arena, F)
    print_results("Buchi", win0, win1, strat0, strat1)

# Co-buchi solver
elif args.game == "cobuchi":
    C = [2, 4, 5, 6, 7, 8]
    win0, strat0, win1, strat1 = cobuchi_solver(arena, C)
    print_results("Co-buchi", win0, win1, strat0, strat1)
