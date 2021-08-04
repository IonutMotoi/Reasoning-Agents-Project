from arena.load_arena import load_arena, load_arena_parity
from tools.output import print_results

from solvers.reachability import reachability_solver
from solvers.safety import safety_solver
from solvers.buchi import buchi_solver
from solvers.cobuchi import cobuchi_solver
from solvers.parity import parity_solver

import argparse

# Create the parser
my_parser = argparse.ArgumentParser(description='Solver for different types of games on graphs')

# Add the arguments
my_parser.add_argument('--game', type=str, required=False, help="The type of game to be solved")
my_parser.add_argument('--arena', type=str, default="assets/arena1.txt", help="Path to the arena txt file")
my_parser.add_argument('--target', type=int, nargs='+', default=None, help="Target set for the game")

# Execute the parse_args() method
args = my_parser.parse_args()

# Reachability solver
if args.game == "reachability":
    arena = load_arena(args.arena)
    R = args.target or [4, 5]
    print("Reachability set =", R)
    (win0, strat0), (win1, strat1) = reachability_solver(arena, R)
    print_results("Reachability", win0, win1, strat0, strat1)

# Safety Solver
elif args.game == "safety":
    arena = load_arena(args.arena)
    S = args.target or [1, 2, 3, 4, 5, 7, 8]
    print("Safety set =", S)
    (win0, strat0), (win1, strat1) = safety_solver(arena, S)
    print_results("Safety", win0, win1, strat0, strat1)

# Buchi solver
elif args.game == "buchi":
    arena = load_arena(args.arena)
    F = args.target or [4, 6]
    print("Recurrence set =", F)
    win0, strat0, win1, strat1 = buchi_solver(arena, F)
    print_results("Buchi", win0, win1, strat0, strat1)

# Co-buchi solver
elif args.game == "cobuchi":
    arena = load_arena(args.arena)
    C = args.target or [2, 4, 5, 6, 7, 8]
    print("Persistence set =", C)
    win0, strat0, win1, strat1 = cobuchi_solver(arena, C)
    print_results("Co-buchi", win0, win1, strat0, strat1)

# Parity solver
elif args.game == "parity":
    arena = load_arena_parity(args.arena)
    parity_solver(arena)
    # win0, win1 = parity_solver(arena)
    # print_results("Parity", win0, win1, [], [])
