
#This is Ui module, here:
#                           1. Tkinter window is created with embeded pygame screen
#                           2. Tkinter buttons are created

from settings import WIDTH, HEIGHT, GAME_SCREEN_WIDTH

import pygame
import tkinter as tk
import os

#function to create and adjust tkinter window
def CreateWindow():

    global root

    root = tk.Tk()

    root.configure(bg='NavajoWhite2')

    root.title("A Star Path Finding Algoritm")

    root.geometry(f"{WIDTH}x{HEIGHT}")

    root.resizable(width=0, height=0)

    #create tkinter embeded frame where pygame window will be placed

    embeded_tkinter_window = tk.Frame(root, width= GAME_SCREEN_WIDTH , height= HEIGHT)
    embeded_tkinter_window.place(x=200, y=0)

    #set enviroment variables to link Pygame With tkinter

    os.environ['SDL_WINDOWID'] = str(embeded_tkinter_window.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    #create pygame Main window

    pygame.init()

    screen = pygame.display.set_mode((1, 1))
    
    return screen, root

#Custom Update root function :)))
def UpdateRoot():
    root.update()

#function to create and display buttons on tkinter window
#   it needs different functions as an attribute for different button commands
def Buttons(start, random, maze, clear, barrier, path, close):
    #create tkinter buttons and locate them:
        #start Button
    button_Start = tk.Button(root, text="Start!", width=20, bd=3, bg="#4CAF50", activebackground="#66BB6A", 
                             command= start)
    button_Start.place(x=20, y=20)

        #Randmom Barriers Button
    button_Random = tk.Button(root, text="Random!", width=20, bd=3, bg="#1E88E5", activebackground="#42A5F5", 
                              command= random)
    button_Random.place(x=20, y=100)

        #Generate Maze Button
    button_GenerateMaze = tk.Button(root, text="Generate Maze", width=20, bd=3, bg="#FF9800", activebackground="#FFB74D",   
                                    command= maze)
    button_GenerateMaze.place(x=20, y=180)

        #Clear Everything Button 
    button_clear = tk.Button(root, text="Clear!", width=20, bd=3, bg="#FFEB3B", activebackground="#FFF176", 
                             command= clear)
    button_clear.place(x=20, y=260)

        #Clear Everrything Except Barriers Button
    button_Only_Barrier = tk.Button(root, text="Only Barrier!", width=20, bd=3, bg="#F44336", activebackground="#EF5350", 
                                    command= barrier)
    button_Only_Barrier.place(x=20, y=340)

        #Show Path Clearly Button
    button_Path = tk.Button(root, text="Show Path!", width=20, bd=3, bg="#9C27B0", activebackground="#BA68C8", 
                            command= path)
    button_Path.place(x=20, y=420)
    
        #Quit from Window Button
    button_Quit = tk.Button(root, text="Quit!", width=20, bd=3, bg="#B71C1C", activebackground="#D32F2F", 
                            command= close)
    button_Quit.place(x=20, y=500)
