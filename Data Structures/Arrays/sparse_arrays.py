#usr/bin/python3

# To create a dictionary you can either use {} or simply use dict() constructor
str_dict = dict()
n = int(input())

while n:
    n-=1
    str_in = input()
    
    # Check if key is present in dict
    # if yes, increment the value of associated with that key
    if str_dict.get(str_in):
        str_dict[str_in]+=1
        continue  # Skip the rest statements, go back to loop
    str_dict[str_in] = 1
    
# input queries
q = int(input())

while q:
    key = input()
    print(str_dict.get(key, 0)) # if present print value, else print 0
    q-=1

    