# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        ans = []
        
        def dfs(node, depth):
            if not node:
                return
            if depth >= len(ans):
                ans.append([])
            ans[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return ans

# Another Approach

def levelOrder(self, root):
	if not(root): return
	s = [root]
	ans = []
	while(len(s)):
		l = len(s)
		temp = []
		for i in range(l):
			t = s.pop(0)
			temp.append(t.val)
			if(t.left):
				s.append(t.left)
			if(t.right):
				s.append(t.right)
		ans.append(temp)
	return ans