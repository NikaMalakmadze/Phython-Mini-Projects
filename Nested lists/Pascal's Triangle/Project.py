#"Pascal's triangle"

n = int(input("Please enter size of Pascal's Triangle: "))                        #getting size of "Pascal's triangle" from user

table = []                                                                          #empty matrix

#create a matrix containing n by n cells
for i in range(n + 1):
    table.append([0] * (n + 1))

#add 1 at the beginning of each row of the matrix
for i in range(n + 1):
    table[i][0] += 1

#Each new cell of the matrix is ​​the sum of the two cells closest to it and above of it
for i in range(1, n + 1):
    for j in range(1, i + 1):
        table[i][j] += table[i - 1][j - 1] + table[i - 1][j]

#printing "Pascal's triangle"
for i in range(n + 1):
    for j in range(i + 1):
        print(table[i][j] , end=" ")
    print()
