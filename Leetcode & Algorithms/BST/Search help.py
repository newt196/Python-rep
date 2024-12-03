#DFS ssearch trea for the future
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def searchDFS(root, value):
    if root is None:
        return False

    if root.data == value:
        return True

    # Search in left and right subtrees
    left_res = searchDFS(root.left, value)
    right_res = searchDFS(root.right, value)
    
    return left_res or right_res

if __name__ == "__main__":
    # 
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.left.left = Node(0)
    root.left.right = Node(1.5)

    value = # whats needed to search through
    if searchDFS(root, value):
        print(f"Value {value} found in the tree!")
    else:
        print(f"Value {value} not found in the tree.")
