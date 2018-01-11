#!/bin/python3

# Take the input, trim the whitespace using strip() and convert the string into integer
# eg: > input() --> '  5 '
#     > strip() --> '5'
#     > int()   -->  5
n = int(input().strip())

# Use list comprehension, split(default=' ') gets a list based on the delimiter specified
# and then converting, each string element in the list to integer
arr = [int(arr_temp) for arr_temp in input().strip().split()]

# Printing elements in Reverse Order
# Can also be done by
# print(arr[::-1])

while n:
    n -= 1
    print(arr[n], end=' ')
