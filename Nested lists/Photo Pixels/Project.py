#Photo Pixels|CodeForces Task|

#The photo is a matrix of size n × m, in each cell of which a symbol is stored, indicating the color of the corresponding pixel. There are 6 colors:
# "C"(cyan) "M"(magenta) "Y"(yellow) "W"(white) "G"(grey) "B"(black)
#A photo can be considered black and white if it contains only white, gray or black color. If at least one pixel of blue, purple or yellow color is present, it is colored.

row , column = map(int, input("Please enter size of your image n x m(pixels):").split())        #getting size of photo from user

matrix = []                                                                                     #create empty matrix

COLORS = "CMYWGB"                                                                               #define avalible colors

CMY_count = 0                                                                                   #colorful colors count

CMY = "CMY"                                                                                     #define colorful colors

stop = False                                                                                    #stop indicator

print(f"Please enter colors of each pixels of your image|Valid Colors:|{COLORS}")

for i in range(row):                                                                            #getting color of each pixel
    matrix.append(input().upper().split())

for i in range(row):
    for j in range(column):
        if matrix[i][j] in COLORS:                                                              #check if color is avalible
            if matrix[i][j] in CMY:                                                                 #check if pixel is colorful color
                CMY_count += 1                                                                              #add count
        else:
            stop = True                                                                         #if colour isn't valid stop indicator - active
            print("Please enter valid colors!")

if stop != True:                                                                                #check stop indicator
    if CMY_count > 0:                                                  #if an image contains only one or more colorful colors, it is colorful image
        print("#Color")
    else:                                                              #if not it's Black&White image
        print("#Black&White")