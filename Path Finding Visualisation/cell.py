
#This is Cell Object Module

from settings import WHITE, RED, GREEN, BLACK, ORANGE, TURQUOISE, PURPLE

import pygame

#create Cell class that will have create a object from every square in grid

#Cell object will have information about:
#1. Its position in Row
#2. Its position in Column
#3. Its color
        #There are 7 colors:
        # WHITE - Empty Cell
        # RED - Closed Cell
        # GREEN - Opened Cell
        # BLACK - Barrier Cell
        # ORANGE - Start Cell
        # TURQUOISE - End Cell
        # PURPLE - Path Cell
#4. Its width, depended on grid size
#5. Its neighbors (ONLY Horizontical AND Vertical)
#6. Total_Number of Rows(size of grid)

class Cell():
    #initialise Cell Object parameters
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = row * width
        self.y = column * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    #Method that returns Cells Location in row and column
    def get_position(self): return self.row, self.column                            
        
    #Method that checks if cell is closed
    def is_closed(self): return self.color == RED
        
    #Method that checks if cell is opened
    def is_open(self): return self.color == GREEN
        
    #Method that checks if cell is barrier
    def is_barrier(self): return self.color == BLACK
        
    #Method that checks if cell is start cell(start point)
    def is_start(self): return self.color == ORANGE
        
    #Method that checks if cell is end cell(end point)
    def is_end(self): return self.color == TURQUOISE
        
    #Method that resets Cell(Makes it empty)
    def reset(self): self.color = WHITE
        
    #Method that makes Cell Closed
    def make_closed(self): self.color = RED
        
    #Method that makes Cell Opened
    def make_open(self): self.color = GREEN
        
    #Method that makes Cell Barrier
    def make_barrier(self): self.color = BLACK
        
    #Method that makes Cell Start Cell(start point)
    def make_start(self): self.color = ORANGE
        
    #Method that makes Cell End Cell(end point)
    def make_end(self): self.color = TURQUOISE
        
    #Method that makes Cell Path
    def make_path(self): self.color = PURPLE
        
    #Method that draws Cell as a square using pygame
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    #Method that gets neighbors of each cell(ONLY Horizonticaly AND Verticaly)
    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.column].is_barrier():         #Down
            self.neighbors.append(grid[self.row + 1][self.column])

        if self.row > 0 and not grid[self.row - 1][self.column].is_barrier():                           #Up
            self.neighbors.append(grid[self.row - 1][self.column])

        if self.column > 0 and not grid[self.row][self.column - 1].is_barrier():                        #Left
            self.neighbors.append(grid[self.row][self.column - 1])

        if self.column < self.total_rows - 1 and not grid[self.row][self.column + 1].is_barrier():      #Right
            self.neighbors.append(grid[self.row][self.column + 1])

    def __lt__(self, other):
        return False