
#This is Utils module, here are some helper functions

from settings import ROWS

from random import randrange
import random

#Function that will randomly pick float from 0 to 1 | So 1 means that cell will be barrier and 0 means that it will not be barrier |
#chance of getting 1 is 50%
def random_barrier():
    if random.random() < 0.5: return 1
    return 0

#Function that will randomly pick cell coordinates on grid
def random_cell():
    return (randrange(0, ROWS), randrange(0, ROWS))
