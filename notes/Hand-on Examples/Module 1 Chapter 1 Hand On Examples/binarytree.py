class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Example Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# In-order Traversal
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

inorder(root)
