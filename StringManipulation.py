"""
String Manipulation Program - write a test case which would take a string as input like 'aabccd' and
print the maximum occurrence of a string in the format a=2,b=1,c=2,d=1
"""
string_input = "aabccd"
max_occ = {}

for i in string_input:
    max_occ[i]=string_input.count(i)

for j in max_occ:
    print(f"{j}={max_occ[j]}", end=" ")