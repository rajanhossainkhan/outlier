def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    #find partition point
    pivot = arr[len(arr) // 2]

    #Apply partition
    left =  [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right =  [x for x in arr if x > pivot]

    #recirsively apply quicksort algorithm
    return quicksort(left) + middle + quicksort(right)

#apply
arr = [64, 34, 25, 12, 22, 11, 90]

print(quicksort(arr))

def quicksort(arr):
    #edge case
    if len(arr) <= 1:
        return arr
    
    #find middle point 
    partition = arr[len(arr) // 2]

    left = [x for x in arr if x < partition]
    middle = [x for x in arr if x == partition]
    right = [x for x in arr if x > partition]

    #apply recursively
    return quicksort(left) + quicksort(middle) + quicksort(right)


