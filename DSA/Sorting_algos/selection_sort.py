# Selection Sort
# Repeatedly finds the smallest element from the unsorted part of the array and swaps it with the first element of the unsorted section.
# Algorithm:
# - Start from the 1st  element and assume it is the smallest.
# - Compare this element with all the remaining elements in the array.
# - If a smaller element is found, update the index of the smallest element. 
# - After the full pass, swap the smallest element found with the first element of the unsorted section.
# - Move to the next element and repeat the process for the remaining unsorted part. 
# - Continue until the entire array is sorted.

arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(arr)-1):
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    
print(arr)