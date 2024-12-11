
#bubble sorting algorithm 

#time complexity O(n 2)        n square

#define function
#it needs unsorted array as an argument
def Bubble_Sort(array):
    #outer loop: iterating throught of array len(array) - 1 times | with one less then its lengh 
    #reasong: after every iteration biggest number of unsorted part of array is moved to right | (So there is no reason to consider them)
    for iteration in range(len(array) - 1):
        #inner loop: comparing elements of array with each other
        #   when outer loop one iteration is complited one biggest element from unsorted part is placed on right side
        #   so reduce inner loop's range by value of iteration variable  
        for element in range(len(array) - 1 - iteration):
            #if current element is greater then next one:
            if array[element] > array[element + 1]:
                #swap this elements
                array[element], array[element + 1] = array[element + 1], array[element]

    return array                        #return sorted array

arr = [34,56,23,5,65,76,34,78,4,29]

print(Bubble_Sort(arr))
