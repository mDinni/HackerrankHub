#usr/bin/python3

# Insert a node at the head of a linked list
# By Dinesh Singh

#Node is defined as
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
    
# Returns the new head
# After inserting a new node at the beginning of linked list
def Insert(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    
    new_node.next = head
    return new_node