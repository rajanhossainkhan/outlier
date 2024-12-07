def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    #find intresection of 2 sets
    intersections = set1.intersection(set2)

    #convert the result back to list
    return list(intersections)


list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

print(find_intersection(list1, list2))
