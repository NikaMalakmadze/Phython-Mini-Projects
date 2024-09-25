#Beautiful matrix |CodeForces Task|
#matrix will look beautiful if the only "1" of this matrix is ​​in its center (in the cell that is at the intersection of the third row and third column). 
#Calculate the minimum number of moves required to make the matrix beautiful.

#using  [x2 - x1] + [y2 - y1] formula to calculate minimal moves requaered to reach center

matrix = []                                              #create empty matrix

for i in range(5):                                                  #input "ugly matrix" using for loop
    matrix.append(list(map(int, input().split())))

for row in range(5):                                                #Go through all the elements of matrix
    for column in range(5):
        if matrix[row][column] == 1:                                 #find "coordinates" of "1" and save it
            x = column
            y = row

distance = round(abs((2 - x)) + abs((2 - y)))                       #find out distance using formula

print(distance)                                                     #print distance
