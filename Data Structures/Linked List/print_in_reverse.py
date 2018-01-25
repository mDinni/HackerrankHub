# Print Linked List in reverse order

# Node is defined as
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Use a recursion approach, the last call will be executed first in stack
def reversePrint(head):
    if head is None:
        return
    reversePrint(head.next)
    print(head.data)