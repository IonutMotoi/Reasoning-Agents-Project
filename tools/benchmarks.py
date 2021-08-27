import argparse
import time
from matplotlib import pyplot as plt
from arena.load_arena import load_arena, load_arena_parity
from solvers.reachability import reachability_solver
from solvers.safety import safety_solver
from solvers.buchi import buchi_solver
from solvers.cobuchi import cobuchi_solver
from solvers.parity import parity_solver_strategy

# Create the parser
my_parser = argparse.ArgumentParser(description='Benchmarks for different types of games on graphs')

# Add the arguments
my_parser.add_argument('--game', type=str, required=False, help="The type of game to be solved")
my_parser.add_argument('--target', type=int, nargs='+', default=None, help="Target set for the game")

# Execute the parse_args() method
args = my_parser.parse_args()

nodes = [10, 100, 1000, 10000]
plt.grid(True)
plt.xlabel("Number of nodes")
plt.xscale("log")
plt.ylabel("Time (s)")
plt.yscale("log")

# Reachability solver
if args.game == "reachability":
    arena0 = load_arena("assets/random_arenas/ran_arena_10_10_2.txt")
    arena1 = load_arena("assets/random_arenas/ran_arena_100_100_20.txt")
    arena2 = load_arena("assets/random_arenas/ran_arena_1000_1000_200.txt")
    arena3 = load_arena("assets/random_arenas/ran_arena_10000_10000_2000.txt")

    R = args.target or [4, 5]
    times = []

    start = time.time()
    win0, strat0, win1, strat1 = reachability_solver(arena0, R)
    times.append(time.time() - start)
    print("Arena0 done")

    start = time.time()
    win0, strat0, win1, strat1 = reachability_solver(arena1, R)
    times.append(time.time() - start)
    print("Arena1 done")

    start = time.time()
    win0, strat0, win1, strat1 = reachability_solver(arena2, R)
    times.append(time.time() - start)
    print("Arena2 done")

    start = time.time()
    win0, strat0, win1, strat1 = reachability_solver(arena3, R)
    times.append(time.time() - start)
    print("Arena3 done")

    print("Reachability times", times)

    plt.plot(nodes, times)
    plt.show()

# Safety Solver
elif args.game == "safety":

    arena0 = load_arena("assets/random_arenas/ran_arena_10_10_2.txt")
    arena1 = load_arena("assets/random_arenas/ran_arena_100_100_20.txt")
    arena2 = load_arena("assets/random_arenas/ran_arena_1000_1000_200.txt")
    arena3 = load_arena("assets/random_arenas/ran_arena_10000_10000_2000.txt")

    S = args.target or [1, 2, 3, 4, 5, 7, 8]
    times = []

    start = time.time()
    win0, strat0, win1, strat1 = safety_solver(arena0, S)
    times.append(time.time() - start)
    print("Arena0 done")

    start = time.time()
    win0, strat0, win1, strat1 = safety_solver(arena1, S)
    times.append(time.time() - start)
    print("Arena1 done")

    start = time.time()
    win0, strat0, win1, strat1 = safety_solver(arena2, S)
    times.append(time.time() - start)
    print("Arena2 done")

    start = time.time()
    win0, strat0, win1, strat1 = safety_solver(arena3, S)
    times.append(time.time() - start)
    print("Arena3 done")

    print("Safety times", times)

# Buchi solver
elif args.game == "buchi":

    arena0 = load_arena("assets/random_arenas/ran_arena_10_10_2.txt")
    arena1 = load_arena("assets/random_arenas/ran_arena_100_100_20.txt")
    arena2 = load_arena("assets/random_arenas/ran_arena_1000_1000_200.txt")
    arena3 = load_arena("assets/random_arenas/ran_arena_10000_10000_2000.txt")

    F = args.target or [4, 6]
    times = []

    start = time.time()
    win0, strat0, win1, strat1 = buchi_solver(arena0, F)
    times.append(time.time() - start)
    print("Arena0 done")

    start = time.time()
    win0, strat0, win1, strat1 = buchi_solver(arena1, F)
    times.append(time.time() - start)
    print("Arena1 done")

    start = time.time()
    win0, strat0, win1, strat1 = buchi_solver(arena2, F)
    times.append(time.time() - start)
    print("Arena2 done")

    start = time.time()
    win0, strat0, win1, strat1 = buchi_solver(arena3, F)
    times.append(time.time() - start)
    print("Arena3 done")

    print("Buchi times", times)

# Co-buchi solver
elif args.game == "cobuchi":

    arena0 = load_arena("assets/random_arenas/ran_arena_10_10_2.txt")
    arena1 = load_arena("assets/random_arenas/ran_arena_100_100_20.txt")
    arena2 = load_arena("assets/random_arenas/ran_arena_1000_1000_200.txt")
    arena3 = load_arena("assets/random_arenas/ran_arena_10000_10000_2000.txt")

    C = args.target or [2, 4, 5, 6, 7, 8]
    times = []

    start = time.time()
    win0, strat0, win1, strat1 = cobuchi_solver(arena0, C)
    times.append(time.time() - start)
    print("Arena0 done")

    start = time.time()
    win0, strat0, win1, strat1 = cobuchi_solver(arena1, C)
    times.append(time.time() - start)
    print("Arena1 done")

    start = time.time()
    win0, strat0, win1, strat1 = cobuchi_solver(arena2, C)
    times.append(time.time() - start)
    print("Arena2 done")

    start = time.time()
    win0, strat0, win1, strat1 = cobuchi_solver(arena3, C)
    times.append(time.time() - start)
    print("Arena3 done")

    print("Co-buchi times", times)

# Parity solver
elif args.game == "parity":
    arena0 = load_arena_parity("assets/random_arenas/ran_arena_10_10_2.txt")
    arena1 = load_arena_parity("assets/random_arenas/ran_arena_100_100_20.txt")
    arena2 = load_arena_parity("assets/random_arenas/ran_arena_1000_1000_200.txt")
    arena3 = load_arena_parity("assets/random_arenas/ran_arena_10000_10000_2000.txt")

    times = []

    start = time.time()
    win0, win1, strat0, strat1 = parity_solver_strategy(arena0)
    times.append(time.time() - start)
    print("Arena0 done")

    print("Parity times", times)

    start = time.time()
    win0, win1, strat0, strat1 = parity_solver_strategy(arena1)
    times.append(time.time() - start)
    print("Arena1 done")

    print("Parity times", times)

    start = time.time()
    win0, win1, strat0, strat1 = parity_solver_strategy(arena2)
    times.append(time.time() - start)
    print("Arena2 done")

    print("Parity times", times)

    start = time.time()
    win0, win1, strat0, strat1 = parity_solver_strategy(arena3)
    times.append(time.time() - start)
    print("Arena3 done")

    print("Parity times", times)

    plt.plot(nodes, times)
    plt.show()
