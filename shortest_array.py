"""
Find out the shortest array and its length from the the array group.
Ex:
Given :  {1,2,3,4},{0,2,7},{4,12},{1,2,5,6}

output:
Shortest Array: {4,12}
Length: 2
"""
arrays = [{1, 2, 3, 4}, {0, 2, 7}, {4, 12}, {1, 2, 5, 6}]
shortest = min([len(i) for i in arrays])

for i in arrays:
    if len(i) == shortest:
        print(f"shortest array is {i}")
        print(f"Length: {arrays.index(i)}")



