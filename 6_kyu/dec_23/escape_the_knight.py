"""
Background

Consider a 8-by-8 chessboard containing only a knight and a king. The knight wants to check the king. The king wants to avoid this. The knight has a cloaking shield, so it moves invisibly. Help the king escape the knight!
Task

You are given the initial king position, initial knight position, and the number of moves n that the titanic struggle will last. Return a list (or array) of length n containing the king's moves. The first move must be a legal king move from the initial king position, and each subsequent move must be a legal king move from the king's previous position. Your goal is for the king to make all the moves in sequence without ever getting checked by the knight, no matter which moves the knight makes.
Details

(1) Squares on the chessboard are specified as strings giving the horizontal coordinate first (a letter from a to h), followed by the vertical coordinate (a number from 1 to 8). Example: On the board below, the knight N is on "d4" and the king K is on "g7".

8 ........         
7 ......K.                 
6 ........                
5 ........              
4 ...N....                 
3 ........               
2 ........                  
1 ........                 
  abcdefgh

(2) The king moves one square in any direction. For example, the king on g7 can move to any of the following squares: f8, f7, f6, g8, g6, h8, h7, h6, as shown below.

8 .....***         
7 .....*K*                 
6 .....***               
5 ........              
4 ........                 
3 ........               
2 ........                  
1 ........                 
  abcdefgh

(3) The knight moves one square horizontally and two squares vertically, or two squares horizontally and one square vertically. For example, the knight on d4 can move to any of the following squares: b3, c2, e2, f3, f5, e6, c6, b5, as shown below.

8 ........         
7 ........                 
6 ..*.*...                
5 .*...*..              
4 ...N....                 
3 .*...*..               
2 ..*.*...                  
1 ........                 
  abcdefgh

(4) The knight and king move simultaneously. The knight wins if it ever checks the king (or if the king moves illegally). The king (and you) win if it survives the specified number of moves without ever being checked.
Example

Given input ("g7", "d4", 6), suppose your function returns ["f8", "e7", "f6", "e7", "d7", "d6"] as the king's moves. If the knight happened to move ["c6", "e5", "g4, "f2", "d1", "e3"], then the knight wins, because after move 3 the knight at g4 checks the king at f6.
Things to Note

(1) The number of moves n satisfies 1 <= n <= 50.

(2) The initial position of the king is always a different square from the initial position of the knight.

(3) It's possible that the knight could be checking the king in the initial position. This is ignored. It's also possible that the same position could occur three times in succession. This is also ignored. (In regular chess this allows a draw to be declared.)

(4) In order to make sure that it never moves to the same square as the king, the knight can access the move-list returned by your function. This means it can use this information when picking its move. (We didn't say this was a fair fight!)
Related Kata

This kata was motivited by Red Knight and Knight vs King.
"""

def get_color(piece):
	return sum([ord(piece[0]) - 96, int(piece[1])]) % 2


def choose_king_moves(king_square, knight_square, number_of_moves):
    trans = str.maketrans("abcdefgh", "badcfehg")
    color = 0 if get_color(king_square) == get_color(knight_square) else 1
    moves = []
    for i in range(number_of_moves):
        king_col = king_square[0].translate(trans)
        king_row = int(king_square[1]) + color if int(king_square[1]) + color <= 8 else 7
        king_square = f"{king_col}{king_row}"
        moves.append(king_square)
        color = 0
    return moves
