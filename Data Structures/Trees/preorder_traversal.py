# Print the tree's preorder traversal as a single line of space-separated values.

# In pre-order tree traversal
# (root, left, right)
def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)
