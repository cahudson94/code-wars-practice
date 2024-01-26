"""
Crazy rabbit is in a coffee field with boundries in an initial given cell (pos = 0 in example). Each field cell might have coffee beans.


  |             |
  |R____________|
   2 2 4 1 5 2 7 # Crazy rabbit at the start"

Crazy rabbit eats all coffee beans that available in the cell. And his jump power increases. Total jump power is equal to the number of total beans eaten

  |             |
  |R____________|
   0 2 4 1 5 2 7 # Crazy rabbit eat coffee beans and his jump power is now 2

Crazy rabbit jumps (initially to the right) if he has a jump power.

     _
  | / \         |
  |R___↓________|
   0 2 4 1 5 2 7 #Crazy rabbit jumps to next position

Crazy rabbit bounces back from a boundries if he jumps too strong


           ___
  |       /   \ |
  |      /     \|
  |     /     / |
  |____R_____↓__|
   0 2 0 1 5 2 7  # next jump will have power of 6, because he ate 4 more coffee beans)

Crazy rabbit position in a field cell is always in the middle. That means that if Crazy rabbit stays right next to the border and have power of jump = 1 then he will be bounced back to the same positon.

After hitting a boundry Crazy rabbit jumps in an opposite direction.

You will be given:

    a field as a list (linear array) of numbers

Can Crazy rabbit eat all the beans? return boolean
"""

def crazyRabbit(field, cr):
    seen = {}
    jump, direction = 0, 1
    available  = {idx for idx, x in enumerate(field) if x and cr != idx}
    while available:
        jump  += field[cr]
        field[cr] = 0
        iteration, cr = divmod(cr + jump * direction, len(field))
        if iteration % 2: 
            direction, cr = -direction, len(field) - cr - 1
        if seen.get((cr, direction)) == jump:
            return False
        available.discard(cr)
        seen[(cr, direction)] = jump
    return True
