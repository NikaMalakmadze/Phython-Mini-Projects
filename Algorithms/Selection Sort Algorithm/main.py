#Selection sorting algorithm 

#time complexity O(n 2)        n square

#define function
#it needs unsorted array as an argument
def selection_sort(array):
    for i in range(0, len(array) - 1):                  #loop from first element to last element not including
        current_minimum_index = i                                   #get index of current minimum element

        for j in range(i + 1, len(array)):                          #start loop from next element after current element to last element
            if array[j] < array[current_minimum_index]:                     #if there is smaller number than current minimum element
                current_minimum_index = j                                           #current minimum index is index of that element

        #swapping smallest element in unsorted part and element with index where this smallest element should go
        #(placing smallest element in correct position)
        array[i], array[current_minimum_index] = array[current_minimum_index], array[i]

    return array

arr = [34,56,23,5,65,76,34,78,4,29]

print(selection_sort(arr))