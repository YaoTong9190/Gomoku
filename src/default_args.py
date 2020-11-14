import argparse

var = argparse.ArgumentParser(
    description='Gomoku Monte-Carlo Tree Search Algorithm')
var.add_argument('--time-limit', default=0.4, type=float)
var.add_argument('--board-size', default=15, type=int)
var.add_argument('--n-in-row', default=5,
                 help='n=5 is the standard Gomoku', type=int)
var.add_argument('--detail', default=False,
                 help='print the Nodes with higher than 0.4 winning rates', type=bool)
var.add_argument('--max-simulation', default=20,
                 help='max simulation for one Node', type=int)
var.add_argument('--max-simulation-one-step', default=150,
                 help='max simulation for one step, used for truncated simulation', type=int)
args = var.parse_args()
