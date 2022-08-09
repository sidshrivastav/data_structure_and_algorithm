from tkinter.messagebox import NO


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def minValueNode(node):
    current = node
  
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
  
    return current

def deleteNode(root, key):
  
    # Base Case
    if root is None:
        return root
  
    # If the key to be deleted 
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
  
    # If the kye to be delete 
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
  
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
  
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
  
        elif root.right is None:
            temp = root.left
            root = None
            return temp
  
        # Node with two children: 
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
  
        # Copy the inorder successor's 
        # content to this node
        root.key = temp.key
  
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
  
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def how_many_bsts(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    _bst = []
    def helper(base, slate = None):
        if len(base) == 0:
            inorder(slate)
            print("\n")
            # _bst.append(slate)
            return
        for j in range(0, len(base)):
            slate = insert(slate, base[j])
            helper(base[:j]+base[j+1:], slate)
            deleteNode(slate, base[j])
            
    n_arr = [i for i in range(1, n+1)]
    # print(n_arr)
    helper(n_arr)
    return _bst

if __name__ == "__main__":
    print(how_many_bsts(3))


# 1 = 1
# 2 = 2
# 3 = 5
# 4 = 
