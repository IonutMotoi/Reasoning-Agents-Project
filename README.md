# Reasoning-Agents-Project

Project for the course of Reasoning Agents at University La Sapienza of Rome A.Y. 2020/2021.

The goal of the project is to implement solvers for different types of games on graphs namely:

- Reachability
- Safety
- Büchi
- Co-Büchi
- Parity

## Description
The user can solve a game by passing as input a game arena as a .txt file with the format shown in the figure:

![Arena example](figs/arena_example.png?raw=true "Arena example")

In the main folder is possible to find the both the [report](Reasoning%20Agents%20Report.pdf) the [slides](Slides%20-%20Games%20on%20Graphs.pdf) that explain in detail the implementation of the algorithms.

## How to run the code
Note : players are called player 0 and player 1
You can try the tool by passing as argument at least '--game' since there are some default values for the arena and the target set.

Here we list some example of commands to run the code:
- To show the help diag: `solver.py -h`
- To solve a game: `solver.py `--game` passing the corresponding game:
  - `--game reachability` for reachability games
  - `--game safety` for safety games
  - `--game Bübuchi` for Büchi games
  - `--game cobuchi` for Co-Büchi games
  - `--game parity` for Parity games
- To specify the arena to solve add the flag: `--arena assets/arena0.txt` with the path that brings to the .txt file containing the arena to solve
- To specify the target set add the flag: `--target 4, 6` with the desired target set (here nodes 4 and 6)

