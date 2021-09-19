from collections import defaultdict
from solvers.buchi import attractor, attractor_with_strategy


def parity_solver(arena):
    win_0 = []
    win_1 = []

    if len(arena.nodes.items()) == 0:
        return win_0, win_1

    # Minimal color occurring in the game
    p = arena.get_max_importance()

    # Parity of the minimal color occurring in the game
    player = p % 2
    opponent = 1 if player == 0 else 0

    if p == 0:
        win_0 = [k for k, v in arena.nodes.items()]
        win_1 = []
        return win_0, win_1

    # Set U of states colored with priority p
    set_u = []
    for node in arena.nodes:
        if arena.get_importance(node) == p:
            set_u.append(node)

    # Attractor A of the region U
    attractor_i = attractor(arena, set_u, player)

    # V \ A
    attractor_i_prime = [x for x in arena.nodes if x not in attractor_i]

    # Create the sub arena
    sub_arena = arena.get_sub_arena(attractor_i_prime)

    if player == 0:
        win_player, win_opponent = parity_solver(sub_arena)
    else:
        win_opponent, win_player = parity_solver(sub_arena)

    if not win_opponent:
        if player == 0:
            win_0.extend([x for x, v in arena.nodes.items()])
        elif player == 1:
            win_1.extend([x for x, v in arena.nodes.items()])
    else:

        attractor_b = attractor(arena, win_opponent, opponent)

        attractor_b_prime = [x for x in arena.nodes if x not in attractor_b]

        sub_arena_2 = arena.get_sub_arena(attractor_b_prime)

        win_player_b, win_opponent_b = parity_solver(sub_arena_2)

        if player == 0:
            win_0.extend(win_player_b)

            win_1.extend(win_opponent_b)
            win_1.extend(attractor_b)
        elif player == 1:
            win_0.extend(win_opponent_b)
            win_0.extend(attractor_b)

            win_1.extend(win_player_b)
    return win_0, win_1


def parity_solver_strategy(arena):
    win_0 = []
    win_1 = []

    strat0 = defaultdict(lambda: -1)  # Winning strategy player 0
    strat1 = defaultdict(lambda: -1)  # Winning strategy player 1

    if len(arena.nodes.items()) == 0:
        return win_0, win_1, strat0, strat1

    # Minimal color occurring in the game
    p = arena.get_max_importance()

    # Parity of the minimal color occurring in the game
    player = p % 2
    opponent = 1 if player == 0 else 0

    if p == 0:
        win_0 = [k for k, v in arena.nodes.items()]
        win_1 = []
        return win_0, win_1, strat0, strat1

    # Set U of states colored with priority p
    set_u = []
    for node in arena.nodes:
        if arena.get_importance(node) == p:
            set_u.append(node)

    # Attractor A of the region U
    attractor_i, strategy_i, _ = attractor_with_strategy(arena, set_u, player)

    # V \ A
    attractor_i_prime = [x for x in arena.nodes if x not in attractor_i]

    # Create the sub arena
    sub_arena = arena.get_sub_arena(attractor_i_prime)

    if player == 0:
        win_player, win_opponent, strat_player, strat_opponent = parity_solver_strategy(sub_arena)
    else:
        win_opponent, win_player, strat_opponent, strat_player = parity_solver_strategy(sub_arena)

    if not win_opponent:
        if player == 0:
            win_0.extend([x for x, v in arena.nodes.items()])
            strat0.update(strategy_i)
            strat0.update(strat_player)
        elif player == 1:
            win_1.extend([x for x, v in arena.nodes.items()])
            strat1.update(strategy_i)
            strat1.update(strat_player)
    else:
        attractor_b, strategy_b, strategy_prova_b = attractor_with_strategy(arena, win_opponent, opponent)

        attractor_b_prime = [x for x in arena.nodes if x not in attractor_b]

        sub_arena_2 = arena.get_sub_arena(attractor_b_prime)

        if player == 0:
            win_player_b, win_opponent_b, strat_player_b, strat_opponent_b = parity_solver_strategy(sub_arena_2)

            win_0.extend(win_player_b)

            win_1.extend(win_opponent_b)
            win_1.extend(attractor_b)

            strat0.update(strat_player_b)

            strat1.update(strategy_b)
            strat1.update(strat_opponent_b)
            strat1.update(strat_opponent)
        else:
            win_opponent_b, win_player_b, strat_opponent_b, strat_player_b = parity_solver_strategy(sub_arena_2)

            win_0.extend(win_opponent_b)
            win_0.extend(attractor_b)

            win_1.extend(win_player_b)

            strat0.update(strategy_b)
            strat0.update(strat_opponent_b)
            strat0.update(strat_opponent)

            strat1.update(strat_player_b)
    return win_0, win_1, strat0, strat1
