#Merge Sort Algorithm
# Merge Sort is a divide and conquer sorting algorithm that splits an array into smaller sub-arrays, sorts them, 
# and then merges them  back together
# Algorithm Steps:
# - Divide: Split the array into 2 halves  recrusively until each subarray contains only one element.
# - Conquer: Sort the subarrays by merging them in sorted order.
# - Combine: Merge the sorted subarrays to form the final sorted array.

def merge_sorting(left,right):
    sorted_array = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i+=1
        else:
            sorted_array.append(right[j])
            j+=1
    
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array
def merge(arr):
    if len(arr)<=1:
        return arr
    mid_element = len(arr)//2
    left_array = merge(arr[:mid_element])
    right_array = merge(arr[mid_element:])
    return merge_sorting(left_array,right_array)

arr = [38, 27, 43, 10]
arr = [64, 34, 25, 12, 22, 11, 90]
print(merge(arr))