#Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0.

# Node is defined as
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def CompareLists(headA, headB):
    if headA is None and headB is None:
        return 1
    elif headA is None or headB is None:
        return 0
    elif headA.data != headB.data:
        return 0
    else:
        return CompareLists(headA.next, headB.next)