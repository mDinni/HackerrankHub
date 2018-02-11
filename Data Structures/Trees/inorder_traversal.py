# Print the tree's inorder traversal as a single line of space-separated values.

# In in-order tree traversal
# (left, root, right)
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)