"""
**Given two sorted arrays, the task is to merge them in a sorted manner .
Example:1
Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8}
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}
Example 2:
Input: arr1[] = { 3,7,9,12,21}, arr2[] = {6,8,15,18,27}
Output: arr3[] = {3,6,7,8,9,12,15,18,21,27}
Time complexity: O(n1+n2) where n1 and n2 are size of each array.
"""
arr1 = {1, 3, 4, 5}
arr2 = {2, 4, 6, 8}

print(arr1.union(arr2))

