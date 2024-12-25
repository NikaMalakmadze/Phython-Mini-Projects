
#This is Algorithms module, also there is heuristic(absolute distance) function and path reconstructing function.
#   Maybe i will add more Algorithms here.

from settings import ITEATION_SPEED, ALGORITHM
from grid import draw

from queue import PriorityQueue

#Heuristic function that can get absolute distance from one point on grid to second point on grid
#it needs both points as arguments
#points are tuples with x and y coordinate of cell
def h(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return abs(x2 - x1) + abs(y2 - y1)

#Function to reconstruct path from end to start point
#it needs came_from dictionary, current(basicly it's end cell but we are starting from end so its current) and draw function to update cells
def reconstruct_path(came_from, current, grid, screen):

    #while current cell is in came_from(while current cell has predecessor)
    while current in came_from:
        #now current cell is predecessor of cell before
        current = came_from[current]

        #make current cell path
        current.make_path()

        #update grid
        draw(grid, screen)
    
    #if current cell is not in came_from dictionary, it means that start point is reached, so make this current cell start point
    current.make_start()

    #indicate that algorithm has finished
    return True

def Algoritm_A_Star(grid, start, end, screen):
    #count variable is needed to manage order of cells in case if two cells have same value(f_score)
    #   So in that case will be selected cell with lowest count(cell that was added earlier in open set )
    count = 0

    #PriorityQueue will help to store cells inside of them.
    #   storing cell as a tuple with f_score, its queue and actual cell object
    #   it is sorting every cell by its f_score
    #       if f_score of cells are same then PriorityQueue is prioritizing cell that was putted first in queue
    open_set = PriorityQueue()                              #create open set
    open_set.put((0, count, start))                         #adding start point into open_set

    #create dictionary that will store path from cell to cell until end point
    #its used to reconstruct path from end to start point
    came_from = {}

    #create dictionary that will store g_score of each cell
    #g_score is cost(path lenght) to reach cell from start point
    #   for default every cell has infinity as a cost of g_score
    #       exception is start point that have 0 as a g_score(since there is no path from start to start point)
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0                                                  #g_score of start point

    #create dictionary that fill store f_score of each cell
    #f_score is calculated by adding g_score to h_score:              |  f_score = g_score + h_score  |
    #   for default every cell has infinity as a cost of f_score
    #       exception is start point that has h_score as a f_score(h_score is absolute distance from start to end point)
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_position(), end.get_position())        #f_Score of start point

    #create open_set_hash that will help to keep track if cell is in open_set without searching it in PriorityQueue
    #   it's a set that has start point at the start
    open_set_hash = {start}

    #variable that helps to keep track number of iterations
    #   its used to update grid after every nth iteration
    step = 0                        

    #run algorithm as long as open_set is not empty 
    while not open_set.empty():
        
        #get current cell to process it
        #get method is getting cell object with lowest f_score(or lowest count)
        current = open_set.get()[2]
        open_set_hash.remove(current)           #remove current cell from open_set_hash because it's being processed

        #if the current cell is end point than algorithm has founded path
        if current == end:
            #call reconstruct_path function to draw path
            reconstruct_path(came_from, end, grid, screen)
            #marking end node visually
            end.make_end()
            #return True(algorithm has ended)
            return True
        
        #loop throught neighbors of current cell
        for neighbor in current.neighbors:
            #calculate temp_g_score of neighbor cell by adding 1 to g_score of current cell
            #   for default on grid 1 is distance from one cell to another
            temp_g_score = g_score[current] + 1

            #if temp_g_score of neighbor is less then its g_score(infinity) in dictionary: 
            if temp_g_score < g_score[neighbor]:
                #add neighbor in came_from dictionary with value - current
                #   so it means that neighbor came from current cell
                came_from[neighbor] = current

                #reassign value of neighbor cell from infinity to its 'real' g_score
                g_score[neighbor] = temp_g_score

                #calculate f_score of neighbor cell by adding temp_g_score to h_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_position(), end.get_position())

                #if neighbor cell is not in open_set_hash
                if neighbor not in open_set_hash:

                    #add 1 to count variable to maintain order in PriorityQueue
                    count += 1

                    #add cell into open_set:    its f_score, order and Cell object
                    open_set.put((f_score[neighbor], count, neighbor))

                    #add cell into open_set_hash to keep track of it
                    open_set_hash.add(neighbor)

                    #make cell open
                    neighbor.make_open()

        #iteration is done, so add 1 to step variable
        step += 1

        #update grid after every 10 iterations
        if step % ITEATION_SPEED == 0:
            draw(grid, screen)

        #if current cell is not start point
        if current != start:
            #mark current cell as closed,because it was processed
            current.make_closed()
    
    return False                                                        #if path was not founded

def Algoritm_Dijkstra(grid, start, end, screen):

    count = 0

    open_set = PriorityQueue()                              #create open set
    open_set.put((0, count, start))                         #adding start point into open_set

    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    open_set_hash = {start}

    step = 0  

    while not open_set.empty():

        current = open_set.get()[2]
        open_set_hash.remove(current)           #remove current cell from open_set_hash because it's being processed

        if current == end:
            #call reconstruct_path function to draw path
            reconstruct_path(came_from, end, grid, screen)
            #marking end node visually
            end.make_end()
            #return True(algorithm has ended)
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                
                came_from[neighbor] = current

                #reassign value of neighbor cell from infinity to its 'real' g_score
                g_score[neighbor] = temp_g_score

                if neighbor not in open_set_hash:

                    #add 1 to count variable to maintain order in PriorityQueue
                    count += 1

                    open_set.put((g_score[neighbor], count, neighbor))

                    #add cell into open_set_hash to keep track of it
                    open_set_hash.add(neighbor)

                    #make cell open
                    neighbor.make_open()

        step += 1

        #update grid after every 10 iterations
        if step % ITEATION_SPEED == 0:
            draw(grid, screen)

        #if current cell is not start point
        if current != start:
            #mark current cell as closed,because it was processed
            current.make_closed()
    
    return False     

def call_algorithm_by_name(grid, start, end, screen):

    if ALGORITHM == 'A_Star': 
        finished = Algoritm_A_Star(grid, start, end, screen)
        if finished:
            return True

    elif ALGORITHM == 'Dijkstra': 
        finished = Algoritm_Dijkstra(grid, start, end, screen)
        if finished:
            return True

    else: return print("Please Enter valid name")
        