"""
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we?
Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]

We want our function to return:

    -1 if the board is not yet finished AND no one has won yet (there are empty spots),
    1 if "X" won,
    2 if "O" won,
    0 if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""

def is_solved(board):
    board_wins = [
    	[(0, 0), (0, 1), (0, 2)], [(0, 0), (1, 0), (2, 0)], [(0, 0), (1, 1), (2, 2)],
    	[(0, 2), (1, 1), (2, 0)], [(0, 2), (1, 2), (2, 2)], [(2, 0), (2, 1), (2, 2)],
    	[(0, 1), (1, 1), (2, 1)], [(1, 0), (1, 1), (1, 2)]
    ]
    for board_win in board_wins:
        if all([board[x][y] == 2 for x, y in board_win]):
            return 2
        if all([board[x][y] == 1 for x, y in board_win]):
            return 1
    if any([0 in row for row in board]):
        return -1
    return 0
