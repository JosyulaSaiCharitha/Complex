"""
/**Given an unsorted array A of size N, find a continuous sub-array which sums up to S.
For example if the input array is [12,7,29,6, 2, 11,4,8] and
the expected sum is 8, then there are two possibilities [6,2] and [8]
if the expected sum is 19 there are two possibilites [12,7] and [6,2,11].
[11,8] is not a possibility since its not continous.
"""

arr = [12, 7, 29, 6, 2, 11, 4, 8]
possibility =[]
num = 19
for i in range(len(arr)-1): # (0,1,2,3,4,5,6,7)
    if arr[i] + arr[i+1] == num:
        print(f"{arr[i],arr[i+1]}")
    elif arr[i]==num:
        print(f"{arr[i]}")
    elif arr[i+1]==num:
        print(f"{arr[i+1]}")



