class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:  
            root.right = self._insert(root.right, key)
        return root

    def in_order_traversal(self, root, result):
        if root:
            self.in_order_traversal(root.left, result)
            result.append(root.key)
            self.in_order_traversal(root.right, result)

def organize_with_bst(arr):
    bst = BST()
    for num in arr:
        bst.insert(num)
    result = []
    bst.in_order_traversal(bst.root, result)
    return result

