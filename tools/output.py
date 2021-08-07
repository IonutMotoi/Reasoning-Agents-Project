import os


def print_results(game, win0, win1, strat0, strat1):
    print(game, "results:")
    print("Winning region player 0", win0)
    print("Winning region player 1", win1)
    print("Strategy player 0", dict(strat0))
    print("Strategy player 1", dict(strat1))


def save_results(game_type, name_arena, win0, win1, strat0, strat1, file=None):
    if file is None:
        if not os.path.exists("output"):
            os.makedirs("output")
        file = "output/" + game_type + "_" + name_arena

    f = open(file, "w")
    f.write(game_type + " results:\n")
    f.write("Winning region player 0: " + str(sorted(win0)) + "\n")
    f.write("Winning region player 1: " + str(sorted(win1)) + "\n")
    f.write("Strategy player 0: " + str(dict(strat0)) + "\n")
    f.write("Strategy player 1: " + str(dict(strat1)) + "\n")
    f.close()
