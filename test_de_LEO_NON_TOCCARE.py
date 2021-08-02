from arena.load_arena import load_arena
from solvers.reachability import reachability_solver
from solvers.safety import safety_solver
from solvers.buchi import buchi_solver
from solvers.cobuchi import cobuchi_solver
import argparse

arena = load_arena("./assets/arena1.txt")

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
    print("Reachability results:")
    print("Winning region player 0", win0)
    print("Strategy player 0", dict(strat0))
    print("Winning region player 1", win1)
    print("Strategy player 1", dict(strat1))


# Safety Solver
if args.game == "safety":
    (winS0, stratS0), (winS1, stratS1) = safety_solver(arena, [1, 2, 3, 4, 5, 7, 8])
    print("Safety results:")
    print("Winning region player 0", winS0)
    print("Strategy player 0", dict(stratS0))
    print("Winning region player 1", winS1)
    print("Strategy player 1", dict(stratS1))


# Buchi solver
if args.game == "buchi":
    F = [4, 6]
    win0, strat0, win1, strat1 = buchi_solver(arena, F)
    print("Buchi solver results:")
    print("Winning region player 0", win0)
    print("Winning region player 1", win1)
    print("Strategy player 0", dict(strat0))
    print("Strategy player 1", dict(strat1))


# Co-buchi solver
if args.game == "cobuchi":
    C = [2, 4, 5, 6, 7, 8]
    print("Co-buchi solver results:")
    win0, strat0, win1, strat1 = cobuchi_solver(arena, C)
    print("Winning region player 0", win0)
    print("Winning region player 1", win1)
    print("Strategy player 0", dict(strat0))
    print("Strategy player 1", dict(strat1))
