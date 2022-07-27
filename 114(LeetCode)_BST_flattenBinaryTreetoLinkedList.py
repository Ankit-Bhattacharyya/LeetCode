#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    def flatten(self, root):
        arr = []
        def dfs(node):
            if not node:
                return None
            arr.append(node.val)
            
            if node.left:
                left = dfs(node.left)
            
            if node.right:
                right = dfs(node.right)
                
        dfs(root)
        if arr:
            root.val = arr.pop(0)
            root.left = None
            root.right = None
            prev = root
        while arr:
            newNode = TreeNode(arr.pop(0))
            prev.right = newNode
            prev = newNode
        return root