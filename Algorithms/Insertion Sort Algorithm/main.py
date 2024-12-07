
#insertion sorting algorithm 

#time complexity O(n 2)        n square

#define function
#it needs unsorted array as an argument
def insertion_sort(array):
    for i in range(1, len(array)):              #looping from second element of array to last element of array
        
        index = i                                               #get index of element
        
        #while the element on the left is greater than the element on the right AND index is greater than 0
        #(not consider the first element)
        while array[index - 1] > arr[index] and index > 0:                             
            array[index - 1], array[index] = array[index], array[index - 1]             #swap this two element with each other
            index -= 1                                                                          #go on left side using index
    
    return array

arr = [34,56,23,5,65,76,34,78,4,29]

print(insertion_sort(arr))