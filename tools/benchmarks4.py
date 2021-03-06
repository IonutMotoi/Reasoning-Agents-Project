import time
from arena.load_arena import load_arena_parity
from solvers.parity import parity_solver_strategy

file = open("output/experiment3.txt", "w")

# Parity solver
for n in range(200, 2200, 200):
    folder_name = "priorityN" + "/nodes" + str(n)
    sum_times = 0
    for i in range(10):
        filename = "assets/random_arenas/" + folder_name + \
                   "/arena_" + str(n) + "_" + str(n) + "_" + str(n) + "_" + str(i) + ".txt"
        arena = load_arena_parity(filename)
        start = time.time()
        win0, win1, strat0, strat1 = parity_solver_strategy(arena)
        sum_times = sum_times + (time.time() - start)
    avg_time = sum_times / 10.0
    print("Average time (arena_" + str(n) + "_" + str(n) + "_" + str(n) + "): " + str(avg_time))
    file.write("Average time (arena_" + str(n) + "_" + str(n) + "_" + str(n) + "): " + str(avg_time) + "\n")

file.close()
