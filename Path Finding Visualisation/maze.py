
#This is Maze module, here:
#                           1. maze is created using mazelib and then it is 'translating' on grid

from grid import make_grid
from settings import ROWS

from mazelib.generate.BacktrackingGenerator import BacktrackingGenerator
from mazelib import Maze

#Function that will generate maze using MazeLib library
#it needs total amount of rows as a argument
def generate_maze_with_mazelib(start, end, grid):
    # Generate maze with mazelib
    maze = Maze()
    maze.generator = BacktrackingGenerator(w=ROWS, h= ROWS)             #set a maze generator and adjust size of maze(same as grid)
    maze.generate()                                                         # Generate a maze

    #Convert maze into list that have rows as a list and every row have cell in it
    #if cell is barrier its value in list is 1
    #if cell is empty its value in list is 0
    maze_grid = maze.grid

    #clear start and end point
    start = None
    end = None

    grid = make_grid()                                                          #clear grid before drawing maze

    #loop throught every cell in grid
    for row in grid:
        for cell in row:
            x, y = cell.get_position()                                      #get position of every cell and unpack it
            if maze_grid[x][y] == 1:                                            #if coordinates of that cell has value 1 in maze_grid
                cell.make_barrier()                                                 #make this cell barrier

    return start, end, grid                                                                     #return start and end points, grid
