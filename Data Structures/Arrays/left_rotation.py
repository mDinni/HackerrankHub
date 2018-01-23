#usr/bin/python3

# Take the input n (no. of elements) and d (no. of rotations to be done) 
n, d = map(int, input().split())

# Store the n elements
a = [int(element) for element in input().strip().split()]

# To rotate the array d times
# => [1 2 3 4 5]
# => Divide it into two parts of size d and n-d
# => Join Second[size_(n-d)] + First[size_(d)]
# => Return the resulted array
def leftRotation(a, d):
    if d == len(a):
        return a
    first_part_arr = a[ :d] 
    second_part_arr = a[d: ]
    return second_part_arr + first_part_arr

result = leftRotation(a, d)
print (" ".join(map(str, result)))