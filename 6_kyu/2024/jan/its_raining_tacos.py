"""
It's Raining Tacos!

A line of tacos is falling out of the sky onto the landscape.

Your task is to predict what the landscape will look like when the tacos fall on it.

                   
INPUT:             
           *********

                   
OUTPUT:    TACOTACOT
           *********

The landscape is represented as any ASCII character, with the air being represented as whitespaces.
The rows are separated by newline characters.

Tacos fall from left to right, distributing the word TACO repeadetly over the landscape.
Each letter falls on the topmost part of the landscape in that area.

If there are no characters in that location, the taco falls all the way to the bottom.

                   
INPUT:       *  ** 
           *** **** 

             C  AC 
OUTPUT:    TA* T**O
           ***O****T

If there is no space for tacos to fall, then that space is skipped.
The next letter still continues forward in the TACO sequence.

           **      
INPUT:     ****    
           ******   

           **CO    
OUTPUT:    ****TA  
           ******COT

Tacos cannot fall through solid material.
If there is a floating island, TACO should be placed on the island, not below it.

                   
INPUT:      *****  
                    

            COTAC 
OUTPUT:     ***** 
          TA     OT

The width and height of the landscape can be anywhere from 1 to 100.

In the case of an empty string, return an empty string.

Good Luck!
"""

def rain_tacos(landscape):
    if not landscape:
        return ""
    cols = list(zip(*landscape.splitlines()))
    tacos = "".join("TACO" * (int(len(cols))))[:len(cols)]
    out = [list(x) for x in cols]
    num_rows = len(out[0])
    for idx, col in enumerate(cols):
        row = 0
        while row < num_rows and col[row] == " ":
            row += 1
        if row == num_rows and col[row - 1] == " ":
            out[idx][row - 1] = tacos[idx]
        elif row < num_rows and row != 0:
            out[idx][row - 1] = tacos[idx]
    return '\n'.join([''.join(out[y][x] for y in range(len(out))) for x in range(num_rows)])

