#Nested list Transpose

n = int(input("Please enter size of yout nested list(n*n): "))      #get size of nested list n by n

list1 = []                                                          #create empty list where nested list will be stored 

print("Your nested list: ")
for i in range(n):                                                  #getting nested list elements using for loop
    list1.append(list(map(int, input().split())))

print()

#Transpose relative to the main diagonal and print it
print("Transpose relative to the main diagonal")
for column in range(n):
    for row in range(n):
        print(list1[row][column], end=" ")
    print()

#Transpose it relative to the side diagonal and print it
print("Transpose it relative to the side diagonal")
for column in range(n - 1, -1, -1):
    for row in range(n - 1, -1, -1):
            print(list1[row][column], end=" ")
    print()
