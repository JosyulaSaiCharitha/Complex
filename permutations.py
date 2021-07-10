"""
If a child is climbing a stair case with “n” steps,
find the maximum number of possibilities (how many different ways he can climb the stair case)
"""
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Returns no. of ways to
# reach sth stair
def countWays(s):
    return fib(s + 1) # fib(4)


# Driver program
s = 3
print("Number of ways = ",countWays(s))