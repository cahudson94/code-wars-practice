"""
Conways game of life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is usually implemented without considering neigbouring cells that would be outside of the arrays range, but another way to do it is by considering the left and right edges of the array to be stitched together, and the top and bottom edges also, yielding a toroidal array and thus all cells get 8 neighbours.

Implement the function get_generation(cells, n) which takes a 2d-array cells an returns generation 'n' of game of life with the initial 'cells' and which considers the array as a toroidal array.

you can use the function print2dArr(list) to print out your array in a more readable format.
Example:

The following pattern would be considered Still life (a pattern which does not change after a generation) on a toroidal array because each live element have exactly 3 neighbours at the toroids stiched edges.

[   1,   0,   0,   1]
[   0,   0,   0,   0]
[   0,   0,   0,   0]
[   1,   0,   0,   1]
"""

class Cell:
    
    def __init__(self, val, x, y):
        self.alive = val == 1
        self.next_state = None
        self.x = x
        self.y = y
        
    def get_next_state(self, cells):
        count = 0
        target_x = [self.x - 1, self.x, self.x + 1]
        target_y = [self.y - 1, self.y, self.y + 1]
        if self.x == len(cells[0]) - 1:
            target_x[2] = 0
        if self.y == len(cells) - 1:
            target_y[2] = 0
        for x in target_x:
            for y in target_y:
                if self.x != x or self.y != y:
                    if cells[y][x].alive:
                        count += 1
        self.next_state = self.alive
        if self.alive and (count < 2 or count > 3):
            self.next_state = False
        elif not self.alive and count == 3:
            self.next_state = True
            
    def next_gen(self):
        self.alive = self.next_state

def get_generation(cells, generation):
    cell_grid = []
    for idx, row in enumerate(cells):
        cell_row = []
        for i, cell in enumerate(row):
            cell_row.append(Cell(cell, i, idx))
        cell_grid.append(cell_row)
    for _ in range(generation):
        for row in cell_grid:
            for cell in row:
                cell.get_next_state(cell_grid)
        for row in cell_grid:
            for cell in row:
                cell.next_gen()
    return [[int(x.alive) for x in row] for row in cell_grid]
