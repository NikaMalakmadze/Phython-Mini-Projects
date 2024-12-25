
#This is Grid module, here are functions: 
#                           1. creating grid and filling with cell objects  
#                           2. drawing grid lines
#                           3. updating each cell's color dynamically
#                           4. getting cell that was clicked

from settings import ROWS, GAME_SCREEN_WIDTH, GREY, WHITE
from cell import Cell

import pygame

GAP = GAME_SCREEN_WIDTH // ROWS                         #get width of Each Cell by dividing width of window on total amount of rows

#Function that creates grid and makes every square of grid Cell Object
#it needs Totat amount of Rows(Grid size) and width of pygame window as a arguments
def make_grid():
    #create empty list of grid
    grid = []
    
    for i in range(ROWS):               #loop throught rows
        grid.append([])                     #append empty list(each row) to grid
        for j in range(ROWS):                   #because width and height are same loop throught rows again
            cell = Cell(i , j, GAP, ROWS)           #create Cell object: i - row;   j - column;   gap - width of cell;   rows - total rows
            grid[i].append(cell)                        #append each cell to its corresponding row

    return grid                                         #return grid

#Function that will draw grid lines on top of Cell objects
#it needs window in where to draw grid, amount of Rows(Grid size) and width of pygame window as a arguments
def draw_grid(screen):

    for i in range(ROWS):                                                   #loop throught rows(or columns, they have same value)
        pygame.draw.line(screen, GREY , (0, i * GAP), 
                         (GAME_SCREEN_WIDTH , i * GAP))    #draw horizontal line from left border to right border of window
        
        pygame.draw.line(screen, GREY , (i * GAP, 0), 
                         (i * GAP, GAME_SCREEN_WIDTH))     #draw vertical line from top border to bottom border
        
#Function that will draw each cell in grid and draw grid using Function 'draw_grid'
#it needs window in where to draw cells and grid, actual grid with cell objects, total amount of rows and width of pygame window -
# - as a arguments
def draw(grid, screen):
    #fill pygame surface(window) with WHITE color
    screen.fill(WHITE)
    for row in grid:                        #loop throught every row in grid
        for cell in row:                        #loop throught every cell in row:
            cell.draw(screen)                       #draw each cell using Cell Object method draw

    #draw grid lines
    draw_grid(screen)
    pygame.display.update()                         #update pygame window

#Function that will 'Translate' position of mouse into rows and columns
#it need position of mouse, total amount of rows and width of pygame window as a arguments
def get_clicked_position(position):

    #position is tuple so unpack it
    x, y = position

    #To find wich cell was clicked:
    row = x // GAP                                      #divide x coordinate on cell width
    column = y // GAP                                   #divide y coordinate on cell width
    return row, column                                      #return x and y
