
# AI Gomoku Game -- CIS667 final project


## Background

> Gomoku, also called Five in a Row, is an abstract strategy board game. It is traditionally played with Go pieces (black and white stones) on a Go board. It can be played using the 15×15 board or the 19×19 board.

**Changed rule:** Each player can either choose to draw a piece or exchange one of the pieces they drew. Instead of placing a new piece, they have the option to choose any one of their pieces on the board, and any one of their opponent's pieces on the board, and then interchange the positions of those two pieces.

**Programming language:** python

**Board size:** 3\*3, 6\*6, 8\*8, 10\*10, 12\*12.

**Game process:**
![process flowchart](https://github.com/YaoTong9190/Gomoku/blob/main/flowchart.png)

## Package pre-install

This project uses [numpy](https://numpy.org) please make sure it has been installed locally.

```
pip install numpy
```

## Usage

The project has constructed by class gomoku, human, baseline, mcts, mcts_nn and other auxiliary files.

src

|- main.py  
|- gomoku.py  
|- human.py  
|- baseline.py  
|- mtcs.py
|- mtcs_nn.py
|- cnn_net.py
|- train.py

To play the game, directly run main.py file.

```
python main.py
```


## Maintainers

[@heyheyhey2020](https://github.com/heyheyhey2020)

[@YaoTong9190](https://github.com/YaoTong9190)

[@xxxhbb](https://github.com/xxxhbb)

## License

## Milestones

- [x] stage1: Basic rule implementation.
- [x] stage2: Tree-based AI implementation.
- [x] stage3: Neural network implementation.
