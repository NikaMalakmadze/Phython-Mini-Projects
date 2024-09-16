#Euclid's Algorithm

#The greatest common divisor (GCD) of two numbers is the greatest common factor number that divides them, exactly

#The principle of the algorithm:

#Let's store the smaller of the two numbers in the variable b
#Then create a while loop that will run until b > 0
#If this condition is fulfilled, assign the value of b to the variable a, and assign the value of operation a % b to the variable b
#And when variable b is not equal to zero while loop stops running
#For the result we get greatest common divisor of this two number

list_a_b = input().split()          #getting numbers from user and storing it in list

New_list = []                       #Temporary list

for num in list_a_b:                #converting every number of list from string to int using for loop
    New_list.append(int(num))
list_a_b = New_list

list_a_b.sort()                     #sorting a list by ascending order

a = list_a_b[1]                     #store biggest number in variable a

b = list_a_b[0]                     #store smallest number in variable b

while b > 0:                        #main principle of algorithm
    a , b = b, a % b

print(f"GCD of numbers: {list_a_b} is {a}")                            #print GCD(greatest common divisor) of this two number 
