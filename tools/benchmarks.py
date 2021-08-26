import argparse
import os
import time
from random_arena import generate_random_arena
from arena.load_arena import load_arena, load_arena_parity
from tools.output import print_results, save_results
from solvers.reachability import reachability_solver
from solvers.safety import safety_solver
from solvers.buchi import buchi_solver
from solvers.cobuchi import cobuchi_solver
from solvers.parity import parity_solver, parity_solver_strategy

# Create the parser
my_parser = argparse.ArgumentParser(description='Benchmarks for different types of games on graphs')

# Add the arguments
my_parser.add_argument('--game', type=str, required=False, help="The type of game to be solved")
my_parser.add_argument('--target', type=int, nargs='+', default=None, help="Target set for the game")

# Execute the parse_args() method
args = my_parser.parse_args()

# Extract the name of the arena from the path
#generate_random_arena(10, 10, 2)
#print("arena0")
#generate_random_arena(100, 100, 20)
#print("arena1")
#generate_random_arena(1000, 1000, 200)
#print("arena2")
#generate_random_arena(10000, 10000, 2000)
#print("arena3")

# Reachability solver
if args.game == "reachability":

    arena0 = load_arena("../assets/random_arenas/ran_arena_10_10_2.txt")
    arena1 = load_arena("../assets/random_arenas/ran_arena_100_100_20.txt")
    arena2 = load_arena("../assets/random_arenas/ran_arena_1000_1000_200.txt")
    arena3 = load_arena("../assets/random_arenas/ran_arena_10000_10000_2000.txt")
    # arena4 = load_arena("../random_arenas/ran_arena_100000_100000_50000.txt")

    R = args.target or [4, 5]
    times = []

    start = time.time()
    win0, strat0, win1, strat1 = reachability_solver(arena0, R)
    times.append(time.time()-start)
    print("Reachability time", times)

    start = time.time()
    win0, strat0, win1, strat1 = reachability_solver(arena1, R)
    times.append(time.time() - start)
    print("Reachability time", times)

    start = time.time()
    win0, strat0, win1, strat1 = reachability_solver(arena2, R)
    times.append(time.time() - start)
    print("Reachability time", times)

    start = time.time()
    win0, strat0, win1, strat1 = reachability_solver(arena3, R)
    times.append(time.time() - start)
    print("Reachability time", times)



# Safety Solver
elif args.game == "safety":

    arena0 = load_arena("../random_arenas/ran_arena_10_10_5.txt")
    arena1 = load_arena("../random_arenas/ran_arena_100_100_50.txt")
    arena2 = load_arena("../random_arenas/ran_arena_1000_1000_500.txt")
    arena3 = load_arena("../random_arenas/ran_arena_10000_10000_5000.txt")
    # arena4 = load_arena("../random_arenas/ran_arena_100000_100000_50000.txt")

    S = args.target or [1, 2, 3, 4, 5, 7, 8]
    print("Safety set =", S)
    start = time.time()
    win0, strat0, win1, strat1 = safety_solver(arena, S)
    safety_time = time.time() - start
    print("Safety time", safety_time)

# Buchi solver
elif args.game == "buchi":

    arena0 = load_arena("../random_arenas/ran_arena_10_10_5.txt")
    arena1 = load_arena("../random_arenas/ran_arena_100_100_50.txt")
    arena2 = load_arena("../random_arenas/ran_arena_1000_1000_500.txt")
    arena3 = load_arena("../random_arenas/ran_arena_10000_10000_5000.txt")
    # arena4 = load_arena("../random_arenas/ran_arena_100000_100000_50000.txt")

    F = args.target or [4, 6]
    print("Recurrence set =", F)
    start = time.time()
    win0, strat0, win1, strat1 = buchi_solver(arena, F)
    buchi_time = time.time() - start
    print("Buchi time", buchi_time)

# Co-buchi solver
elif args.game == "cobuchi":

    arena0 = load_arena("../random_arenas/ran_arena_10_10_5.txt")
    arena1 = load_arena("../random_arenas/ran_arena_100_100_50.txt")
    arena2 = load_arena("../random_arenas/ran_arena_1000_1000_500.txt")
    arena3 = load_arena("../random_arenas/ran_arena_10000_10000_5000.txt")
    # arena4 = load_arena("../random_arenas/ran_arena_100000_100000_50000.txt")

    C = args.target or [2, 4, 5, 6, 7, 8]
    print("Persistence set =", C)
    start = time.time()
    win0, strat0, win1, strat1 = cobuchi_solver(arena, C)
    cobuchi_time = time.time() - start
    print("Co-Buchi time", cobuchi_time)


# Parity solver
elif args.game == "parity":

    arena0 = load_arena_parity("../random_arenas/ran_arena_10_10_5.txt")
    arena1 = load_arena_parity("../random_arenas/ran_arena_100_100_50.txt")
    arena2 = load_arena_parity("../random_arenas/ran_arena_1000_1000_500.txt")
    arena3 = load_arena_parity("../random_arenas/ran_arena_10000_10000_5000.txt")
    # arena4 = load_arena_parity("../random_arenas/ran_arena_100000_100000_50000.txt")

    start = time.time()
    win0, win1, strat0, strat1 = parity_solver_strategy(arena0)
    parity_time = time.time() - start
    print("Parity time", parity_time)




