---
---

# AI Gomoku Game -- CIS667 final project

---

## Background

> Gomoku, also called Five in a Row, is an abstract strategy board game. It is traditionally played with Go pieces (black and white stones) on a Go board. It can be played using the 15×15 board or the 19×19 board.

**Changed rule:** Each player can either choose to draw a piece or exchange one of the pieces they drew. Instead of placing a new piece, they have the option to choose any one of their pieces on the board, and any one of their opponent's pieces on the board, and then interchange the positions of those two pieces.

**Programming language:** python

**Board size:** 15\*15

**Game process:**
![process flowchart](https://github.com/YaoTong9190/Gomoku/blob/main/flowchart_milestone2.png)

## Package pre-install

This project uses [numpy](https://numpy.org),[argparse](https://pypi.org/project/argparse/) please make sure it has been installed locally.

```
pip install numpy
pip install argparse
```

## Usage

The project has constructed by class board, node, tree search algorithm and other auxiliary file to parse argument

src

|- main.py  
|- board.py  
|- node.py  
|- tree_algorithm.py  
|- default_args.py

```
python main.py
```

optional parameter

```
--detail true/false (print nodes processed in each step)
--time-limit  (simulations will end when time is up)
--board-size (the standard is 15 by 15)
--max-simulation (the max simulation for one node)
--max-simulation-one-step (max simulation for one step, depth simulation times)
```

## Maintainers

[@heyheyhey2020](https://github.com/heyheyhey2020)

[@YaoTong9190](https://github.com/YaoTong9190)

[@xxxhbb](https://github.com/xxxhbb)

## License

## Milestones

- [x] stage1: Basic rule implementation.
- [x] stage2: Tree-based AI implementation.
- [ ] stage3: Neural network implementation.
