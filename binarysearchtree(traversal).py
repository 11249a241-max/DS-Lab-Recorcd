class BSTNode:
    def __init__(self, v):
        self.v = v; self.left = None; self.right = None

def bst_insert(root, v):
    if not root: return BSTNode(v)
    if v < root.v: root.left = bst_insert(root.left, v)
    else: root.right = bst_insert(root.right, v)
    return root

def inorder(root):
    return inorder(root.left)+[root.v]+inorder(root.right) if root else []
def preorder(root):
    return [root.v]+preorder(root.left)+preorder(root.right) if root else []
def postorder(root):
    return postorder(root.left)+postorder(root.right)+[root.v] if root else []

if __name__ == "__main__":
    vals = [5,3,7,2,4,6,8]
    r = None
    for x in vals: r = bst_insert(r, x)
    print(inorder(r)); print(preorder(r)); print(postorder(r))
