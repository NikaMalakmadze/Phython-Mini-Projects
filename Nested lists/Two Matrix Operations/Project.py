#Two Matrix Sum, Difference and Multiply calculator

#Program validity condition
print("This is program that calculates sum, difference and multiply of two matrices!")                                         
print("P.S They should have same number of Rows and Columns!")
rows, columns = map(int, input("Please input Rows and Columns number for matrix: ").split())        #getting number of rows and columns of matrix

matrix1 = []                                                                                        #empty list for first matrix

matrix2 = []                                                                                        #empty list for second matrix

print("Matrix N1")
for i in range(rows):                                                                               #getting elements of first matrix
    row = list(map(int, input().split()))
    matrix1.append(row)

print()
input("Press Enter")                                                                                #to paste matrices from sites and etc.
print()

print("Matrix N2")                                                                                  
for i in range(rows):                                                                                #getting elements of second matrix
    row = list(map(int, input().split()))
    matrix2.append(row)

print("Sum:")
for i in range(rows):                                                                               #calculating sum of matrices
    for j in range(columns):
        print(matrix1[i][j] + matrix2[i][j], end=" ")
    print()

print("Difference:")
for i in range(rows):                                                                               #calculating difference of matrices
    for j in range(columns):
        print(matrix1[i][j] - matrix2[i][j], end=" ")
    print()

print("Multiply:")
for i in range(rows):                                                                               #calculating multiply of matrices
    for j in range(columns):
        print(matrix1[i][j] * matrix2[i][j], end=" ")
    print()
