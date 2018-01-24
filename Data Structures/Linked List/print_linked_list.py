#usr/bin/python3

# Node is defined as
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Printing the elements of linked list
def print_list(head):
    while head:         # if still there's a node loop
        print(head.data)   
        head = head.next    # Now refer to the next node 
