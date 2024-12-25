
#This is Main module, here:
#                               1. everything is combined together
#                               2. here are 'commands' for tkinter buttons

from grid import make_grid, draw, get_clicked_position
from ui import CreateWindow, UpdateRoot, Buttons
from algorithms import call_algorithm_by_name
from utils import random_cell, random_barrier
from maze import generate_maze_with_mazelib

import pygame

#Function that will start algorithm when its tkinter button is clicked 
def start_on_click():
    global screen, FINISHED
    #function will start only then, when start and end points are placed
    if start and end:
        #loop throught every cell on grid
        for row in grid:
            for cell in row:
                cell.update_neighbors(grid)                 #get neighbors of every cell on grid for working of algorithm 

        #Call Algorithm function
        FINISHED = call_algorithm_by_name(grid, start, end, screen)

#Function that will end program when clicking on exit button
def close_on_click():
    global running
    running = False
    pygame.quit()                                                   #quit from pygame
    root.quit()                                                         #quit from root(tkinter)

#Function that will clear the grid:
def clear_grid():
    global grid, start, end                     #get variables from global
    #reset start and end points
    start = None
    end = None
    grid = make_grid()                          #recreate grid

#Function that will create barriers on grid randomly when its tkinter button is clicked
def random_on_click():
    global grid

    clear_grid()                                #clear the grid first
    #loop throught every cell on grid
    for row in grid:
        for cell in row:
            x, y = random_cell()                                    #get coordinates of random cell and unpack them
            if not cell.is_barrier() and random_barrier() == 1:             #if that cell is not barrier and it has 'weight' of barrier
                grid[x][y].make_barrier()                                           #make cell with those coordinates barrier

#Function that will generate and draw maze on grid
def regenerate_maze_on_click():
    global grid, start, end, screen

    start, end, grid = generate_maze_with_mazelib(start, end, grid)                 #regenerate the maze and update the grid
    
    draw(grid, screen)                                                                                  #redraw the grid immediately

#Function that will clear open and closed cells, so it will show path clearly
def path():
    global FINISHED, grid
    #function will start only if algorithm is finished
    if FINISHED:
        #loop throught every cell in grid
        for row in grid:
            for cell in row:
                if cell.is_open() or cell.is_closed():                          #if cell is closed or open:
                    cell.reset()                                                    #reset it(make empty)

#Function that will clear everything except barrier cells
def only_barrier_on_click():
    global start, end, grid                                       #get global variables
    #reset start and end point
    start = None
    end = None
    #loop throught every cell in grid
    for row in grid:
        for cell in row:
            if not cell.is_barrier():                       #if cell is not barrier
                cell.reset()                                    #reset this cell(make empty)

#Main function
def main():
    global start, end, grid, FINISHED, screen, root, running            #set global variables

    #create tkinter window and get pygame screen and tkinter root
    screen, root = CreateWindow()
    
    #set closing function when X button on tkinter window is clicked
    root.protocol('WM_DELETE_WINDOW', close_on_click)

    #create empty grid
    grid = make_grid()

    #empty start and end points
    start = None
    end = None

    running = True                                                  #indicates if code is running
    FINISHED = None                                                 #indicates if algorithm ended working

    #create and display buttons
    #   also give functions as a 'commands' for a buttons
    Buttons(
        lambda: start_on_click(),
        lambda: random_on_click(),
        lambda: regenerate_maze_on_click(),
        lambda: clear_grid(),
        lambda: only_barrier_on_click(),
        lambda: path(),
        lambda: close_on_click()
    )

    #main loop
    while running:
        draw(grid, screen)                              #update grid
        for _ in pygame.event.get():                        #get pygame events

                if pygame.mouse.get_pressed()[0]:               #when clicked on mouse left button
                    pos = pygame.mouse.get_pos()                            #get position of mouse
                    row, col = get_clicked_position(pos)           #'Translate' it into rows and columns
                    cell = grid[row][col]                                           #Pick cell that was clicked
                    if not start:                                                       #if there is no start point
                        start = cell                                                        #make start variable Cell object
                        start.make_start()                                                      #make that cell start point

                    elif not end:                                                       #if there is no end point
                        end = cell                                                          #make end variable Cell object
                        end.make_end()                                                          #make that cell end point

                    elif cell != start and cell != end:                                 #if both start and end points were placed
                        cell.make_barrier()                                                 #make that cell barrier

                elif pygame.mouse.get_pressed()[2]:             #when clicked on mouse right button
                    pos = pygame.mouse.get_pos()                            #get position of mouse
                    row, col = get_clicked_position(pos)           #'Translate' it into rows and columns
                    cell = grid[row][col]                                           #Pick cell that was clicked
                    cell.reset()                                                        #reset that cell(make empty)
                    if cell == start:                                                       #if clicked on start point
                        start = None                                                            #reset start variable
                    elif cell == end:                                                       #if clicked on end point
                        end = None                                                              #reset end variable
        
        UpdateRoot()    #update root
        
if __name__ == '__main__':
    main()