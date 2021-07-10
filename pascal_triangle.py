"""
Print Pascal Triangle , print the value for the given co-orinates
Ex:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
Given: Co-Orinates(3,2) means answer should be : 2
"""
# def solve(A):
k,l = 5,2

pascals_triangle = []
for i in range(k+1): # 0,1,2,3
    pascals_triangle.append([1] * (i + 1)) # [[1],[1,1],[1,1,1],[1,1,1,1]]

for i in range(2, k+1): # 2,3
    for j in range(1, i): # 1 1,2
        pascals_triangle[i][j] = pascals_triangle[i - 1][j - 1] + pascals_triangle[i - 1][j]

    # return pascals_triangle
print(pascals_triangle)
print(pascals_triangle[k-1][l-1])

