class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None or root.val > 10000:
            return None
        self.count = 0
        self.result = None

        def to_order(node):
            if not node or self.result is not None:
                return
            
            to_order(node.left)
            
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            

        to_order(root)
        return self.result
