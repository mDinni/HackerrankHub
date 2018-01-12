#!usr/bin/python3


# List comprehension is used to create a 2d matrix or list
# Input is a 6*6 matrix where -9 <= A(i,j) <= 9 
arr = [[int(element) for element in input().strip().split()] for i in range(6)]

# Minimum sum of hourglass is -9*7 = -63
max = -63

for i in range(4):
    for j in range(4):
        sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        sum += arr[i+1][j+1]
        sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        
        # Comparing previous max is still maximum if not then..
        if max < sum:
            max = sum

print(max)