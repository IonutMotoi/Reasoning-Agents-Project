from collections import defaultdict
from solvers.buchi import attractor
import copy


def parity_solver(arena):
    win_0 = []
    win_1 = []

    # Minimal color occurring in the game
    p = arena.get_max_importance()
    print("MAX IMPORTANCE", p)

    # Parity of the minimal color occurring in the game
    player = p % 2
    opponent = 1 if player == 0 else 0

    if p == 0:
        win_0 = [k for k, v in arena.nodes.items()]
        win_1 = []
        return win_0, win_1
    else:
        # Set U of states colored with priority p
        set_u = []
        for node in arena.nodes:
            if arena.get_importance(node) == p:
                set_u.append(node)
        print("Set U =", set_u)

    # # Attractor A of the region U
    # attractor_i = attractor(arena, set_d, i)
    # print("Attractor region player", i, ":", attractor_i)
    #
    # # V \ A
    # attractor_i_prime = [x for x in nodes if x not in attractor_i]
    # print("A_prime =", attractor_i_prime)
    #
    # # Case 1 -> A = V
    # if not attractor_i_prime:
    #     print("CASE 1")
    #     if i == 0:
    #         win_player0 = [x for x in nodes]
    #         win_player1 = []
    #     elif i == 1:
    #         win_player0 = []
    #         win_player1 = [x for x in nodes]
    #     return win_player0, win_player1
    # # Case 2 -> A != V
    # else:
    #     print("CASE 2")
    #     copy_arena = copy.copy(arena)
    #     sub_arena = copy_arena.get_sub_arena(attractor_i_prime)
    #     win_player0, win_player1 = parity_solver(sub_arena)
    #     print("CONT. CASE 2")
    #     print("win_player0", win_player0, "win_player1", win_player1)
    #
    #     # Subcase 1 -> win_player1 is empty set
    #     if not win_player1:
    #         print("SUBCASE 1")
    #         win_player0 = [x for x in nodes]
    #         win_player1 = []
    #         return win_player0, win_player1
    #
    #     # Subcase 2 -> win_player1 not empty set
    #     else:
    #         print("SUBCASE 2")
    #
    #         attractor_b = attractor(sub_arena, win_player1, 1 if i == 0 else 0)
    #         print("attractor_b =", attractor_b)
    #         attractor_b_prime = [x for x in nodes if x not in attractor_b]
    #         print("B_prime =", attractor_b_prime)
    #
    #         copy_arena_2 = copy.copy(copy_arena)
    #         sub_arena_2 = copy_arena_2.get_sub_arena(attractor_b_prime)
    #         win_player0_b, win_player1_b = parity_solver(sub_arena_2)
    #         print("CONT. SUBCASE 2")
    #         win_player1.extend(win_player1_b)
    #         return win_player0, win_player1
