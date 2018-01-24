#usr/bin/python3

# Insert Node at a specific position in a linked list
# By Dinesh Singh

#Node is defined as
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Returns the head of the linked list after insertion of node
# at specific position
def insertNth(head, data, position):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head

    if position == 0:
        new_node.next = head
        return new_node
    
    count = 1
    current_node = head
    while (current.next is not None and count < position):
        current_node = current_node.next
        count += 1
    
    # Insert node at the given position
    tmp_position_node = current_node.next
    current_node.next = new_node
    new_node.next = tmp_position_node

    return head 
    