# Print the tree's postorder traversal as a single line of space-separated values.

# In post-order tree traversal
# (left, right, root)
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)