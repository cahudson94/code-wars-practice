"""
You have to write a function that takes for input a 8x8 chessboard in the form of a bi-dimensional array of chars (or strings of length 1, depending on the language) and returns a boolean indicating whether the king is in check.

The array will include 64 squares which can contain the following characters :

    '♔' for the black King;
    '♛' for a white Queen;
    '♝' for a white Bishop;
    '♞' for a white Knight;
    '♜' for a white Rook;
    '♟' for a white Pawn;
    ' ' (a space) if there is no piece on that square.

Note : these are actually inverted-color chess Unicode characters because the codewars dark theme makes the white appear black and vice versa. Use the characters shown above.

There will always be exactly one king, which is the black king, whereas all the other pieces are white.
The board is oriented from Black's perspective.
Remember that pawns can only move and take forward.
Also be careful with the pieces' lines of sight ;-) .

The input will always be valid, no need to validate it. To help you visualize the position, tests will print a chessboard to show you the problematic cases. Looking like this :

|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   | ♜ |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   | ♔ |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
"""

def is_check(piece, space, king):
    if piece == "♟":
        if king[0] - space[0] == 1 and abs(space[1] - king[1]) == 1:
            return True
    if piece == "♞":
        if abs(space[0] - king[0]) + abs(space[1] - king[1]) == 3 and space[0] != king[0] and space[1] != king[1]:
            return True
    if piece == "♝":
        if sum(space) == sum(king):
            return True
        if king[0] > space[0]:
            while king[0]:
                if king == space:
                    return True
                king = king[0] - 1, king[1] - 1
        else:
            while space[0]:
                if space == king:
                    return True
                space = space[0] - 1, space[1] - 1
    if piece == "♜":
        if space[0] == king[0] or space[1] == king[1]:
            return True
    if piece == "♛":
        if space[0] == king[0] or space[1] == king[1] or sum(space) == sum(king):
            return True
        if king[0] > space[0]:
            while king[0]:
                if king == space:
                    return True
                king = king[0] - 1, king[1] - 1
        else:
            while space[0]:
                if space == king:
                    return True
                space = space[0] - 1, space[1] - 1
    return False

def is_blocked(piece, space, pieces, king):
    spaces = []
    if piece == "♝":
        num_spaces = abs(king[0] - space[0]) - 1
        spaces = [(max(space) - x, min(space) + x) for x in range(1, num_spaces + 1)]
    if piece == "♜":
        if king[0] == space[0]:
            num_spaces = abs(king[1] - space[1]) - 1
            spaces = [(king[0], max(space[1], king[1]) - x) for x in range(1, num_spaces + 1)]
        else:
            num_spaces = abs(king[0] - space[0]) - 1
            spaces = [(max(space[0], king[0]) - x, king[1]) for x in range(1, num_spaces + 1)]
    if piece == "♛":
        if king[0] == space[0]:
            num_spaces = abs(king[1] - space[1]) - 1
            spaces = [(king[0], max(space[1], king[1]) - x) for x in range(1, num_spaces + 1)]
        elif king[1] == space[1]:
            num_spaces = abs(king[0] - space[0]) - 1
            spaces = [(max(space[0], king[0]) - x, king[1]) for x in range(1, num_spaces + 1)]
        else:
            num_spaces = abs(king[0] - space[0]) - 1
            spaces = [(max(space) - x, min(space) + x) for x in range(1, num_spaces + 1)]
    print(spaces)
    for space in spaces:
        for b_space, blocker in pieces.items():
            if blocker != piece:
                if space == b_space:
                    return True
    return False

def king_is_in_check(chessboard : list[list[str]]) -> bool:
    """ do your magic (; """
    pieces = {(idx, i): piece for idx, row in enumerate(chessboard) for i, piece in enumerate(row) if piece != " "}
    king = [xy for xy, piece in pieces.items() if piece == "♔"][0]
    del pieces[king]
    for space, piece in pieces.items():
        if is_check(piece, space, king):
            print(space, piece)
            if not is_blocked(piece, space, pieces, king):
                return True
    return False
