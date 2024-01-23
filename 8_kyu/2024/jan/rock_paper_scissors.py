"""
Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
"""

def rps(p1, p2):
    wins = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    return "Draw!" if p1 == p2 else "Player 1 won!" if wins[p1] == p2 else "Player 2 won!"
