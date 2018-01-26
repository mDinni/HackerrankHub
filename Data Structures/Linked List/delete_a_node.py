#Delete the node at the given position and return the head of the updated linked list.

# Node is defined as
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def delete(head, position):
    
    if position is 0:
        return head.next

    head.next = Delete(head.next, position-1)
    return head