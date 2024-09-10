#Number list Info

print("------------------------------------------")         #decoration
print("--------Please input only integers--------")         #decoration
print("------------------------------------------")         #decoration

list_num = int(input("Please enter number of list elements: "))         #get size of list from user

print("------------------------------------------")         #decoration

list_element = input("Please enter list elements(Numbers only): ").split()      #get elements of list and split it

list = []           #create a empty list

for i in range(list_num):               #for loop for every element of this list
    take_out = list_element.pop()       #take out last element from user input list with method pop
    list.append(int(take_out))          #put it in empty list with method append

mult = 1            #create a variable with which we will multiply numbers

for numbers in list:            #multiply every number of list on each other using for loop
    mult = mult * numbers       #multiply current value of variable mult with the new one

sum = sum(list)                 #find out the sum of each element of the list
max = max(list)                 #find out biggest number of list
min = min(list)                 #find out smallest number of list

print("-------------------info-------------------")         #decoration

print(f"Numbers you entered: {list}")

list.sort()                                                                 #sort a list in ascending order
                                                                
print(f"The numbers you enter are sorted in ascending order: {list}")

list.sort(reverse= True)                                                    #sort a list in descending order

print(f"The numbers you enter are sorted in descending order: {list}")
print(f"Sum of all numbers: {sum}")
print(f"Multiply of all numbers: {mult}")
print(f"Biggest number from your list: {max}")
print(f"Smallest number from your list: {min}")

print("------------------------------------------")         #decoration