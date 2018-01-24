# Insert a node at the Tail of a Linked List

# Node is defined as
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Returns back the current head of the linked list after insertion
def Insert(head, data):
    # Create a new node with given data
    new_node = Node(data)
    
    if head is None:
        head = new_node
        return head
    
    current_node = head
    while current_node.next is not None:
        current_node = current_node.next
    
    # As we are at the end of the linked list after while loop
    # assign new node to the current node
    current_node.next = new_node 
    return head
