"""
Connect Four

Take a look at wiki description of Connect Four game:

Wiki Connect Four

The grid is 6 row by 7 columns, those being named from A to G.

You will receive a list of strings showing the order of the pieces which dropped in columns:

  pieces_position_list = ["A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "G_Red",
                          "B_Yellow"]

The list may contain up to 42 moves and shows the order the players are playing.

The first player who connects four items of the same color is the winner.

You should return "Yellow", "Red" or "Draw" accordingly.

note:
Cheating is permitted in the random tests.
"""

def is_win(player, board, col, row):
    board_col = list(zip(*board))[col][row + 6:row + 10]
    if all(x == player for x in board_col) and len(board_col) >= 4:
        return True
    count = 0
    for x in board[row]:
        if x == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0

    x, y = col, row + 6
    diags = [[], []]
    for i in range(7):
        if y - x + i >= 0 and y - x + i <= 5:
            diags[0].append(board[y - x + i][i])
        if x + y - i >= 0 and x + y - i <= 5:
            diags[1].append(board[x + y - i][i])
    for diag in diags:
        count = 0
        for x in diag:
            if x == player:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0


def who_is_winner(pieces_position_list):
    board = [[0 for _ in range(7)] for _ in range(6)]
    for i, x in enumerate(pieces_position_list):
        move, player = x.split("_")
        player = 1 if player == "Yellow" else 2
        move = ord(move) - 65
        for idx, y in enumerate(list(zip(*board))[move][::-1]):
            if y:
                continue
            board[-idx - 1][move] = player
            break
        if i > 3 and is_win(player, board, move, -idx - 1):
            return "Yellow" if player == 1 else "Red"
    return "Draw"
