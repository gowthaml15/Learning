# Insertion Sort Algoritm
#Insertion Sort works by building a sorted section of the array one at a time. 
# It picks elements from the unsorted section and places them in their correct position within the sorted section.
#Algorithm
# - Start with the second element(index 1).
# - Pick the current element and compare it with the elements in the sorted sections( on the left). 
# - Shift all larger elements one position to the right to make space.
# - Insert the picked element into its correct position.
# - Repeat this process for all element in the array.
# Time Complexity:
# Best case ( Sorted Array): O(n)
# Worst /Average case: O(n^2) (when shifting elements frequently)
#Space Complexity:
# O(1) -> Constant space
# arr = [5, 3, 8, 6, 2]
# arr = [1, 2, 3, 4, 5]
arr = [9, 7, 5, 3, 1]
for i in range(1, len(arr)):
    key = arr[i]
    for j in range(i-1,-2,-1):
        if arr[j]>key:
            arr[j+1] = arr[j]
        else:
            break
    arr[j+1] = key
print(arr)

