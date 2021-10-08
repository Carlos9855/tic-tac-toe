
# Sistemas-inteligentes-Practice-5
# tic-tac-toe
## Members
* Jose Carlos Camacho Salazar
* Diego Delgadillo Cabrera
* Sebastian Lazarte Catellon

# Problem Description
An intelligent N in line has to be programmed, in this case a human will face a computer. The intelligent program must make an "intelligent" decision on where to place the chip in a reasonable time and in a reasonable time.

# Solution Description
The game logic was implemented so that it works on a board with 3x3, 4x4 and 5x5 dimensions.

The minmax algorithm was implemented, which consists in choosing the best move to be chosen by the machine assuming that the opponent will choose the best option. The algorithm generates and runs through a game tree of solutions (game tree) of the game, starting from a state 

Alpha beta pruning is not a new algorithm, it is an optimization technique that is used in the min max algorithm. This optimization does not expand the whole tree of states but accesses a final state that is at a certain height.

# Running the script
To run this application, you need to install Python3 and pygame. Assuming Python3 is installed, to install pygame run:

```
$ pip3 install pygame
```

In order to run the program you first have to enter the 
directory where the `menu.py` file is located through 
the ***CMD*** console or the one of your choice.

```
$ python3 menu.py
```
# Experiments

A series of experiments were performed to test the functionality of the algorithms and that everything works in the best possible way, in these experiments the time it took the ia to decide its next move was verified, and also the spanning tree was measured.

![1](https://user-images.githubusercontent.com/58644744/136495655-2f7cfe3d-c761-48ec-b7b9-c3df6692e785.png)

This first experiment is about playing in easy mode and letting the IA to win.

![2](https://user-images.githubusercontent.com/58644744/136495668-f1691259-204f-4118-bf2b-f45d0e22221f.png)

This second experiment is using Cutoff and playing as the "O" so the IA can play first.

![3](https://user-images.githubusercontent.com/58644744/136495678-3d74b735-887b-4525-8199-0aa5e42d072a.png)

This experiment is playing with minmax and the result is a draw.

## How many states does the game tree have for a board of dimensions 3x3, 4x4 and 5x5?

The number of tree expansion states is defined by the number of empty squares in the move.
This means that in each new AI turn, the AI only expands the number of nodes that are empty, which means that in each move the number of nodes to be expanded decreases by two.

## Which algorithm takes the most (least) time and expands the most (least) number of states? MinMax, MinMax + AlphaBeta Prunning or MinMaxCutoff?




# Conclusions

we have observed that by varying the dimensions of the board, some algorithms take longer to run and therefore the games take longer than they should.

# Recommendations

it is recommended to have a more or less powerful computer 

#Reference

* Class slides
* https://github.com/laurakoco/tic-tac-toe-ai
