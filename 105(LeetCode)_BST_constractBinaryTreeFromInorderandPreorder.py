class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
                                # The plan:
                                #   • use preorder[0] as root, then determine root's left and right
                                #     subtrees from root's index in inorder.
                                #   • with the preorder and inorder for each subtree, determine that 
                                #     subtree recursively

                                # There's an example below the code:
                                #          preorder = [4,6,1,7,5,2], and inorder = [1,6,7,4,5,2]

    def buildTree(self, preorder, inorder):
        if not preorder: return None                            # <- handle the base case.

        root = TreeNode(preorder[0])                            # <- identify the root
        idx = inorder.index(root.val)                           # <- determine index of the root in inorder
   
        leftIn, rightIn = inorder[:idx],  inorder[idx+1:]       # <- determine inorders  for the subtrees 
        leftPr, rightPr = preorder[1:idx+1], preorder[idx+1:]   # <- determine preorders for the subtrees

        root.left  = self.buildTree(leftPr,  leftIn )           # <- left and right recursive calls
        root.right = self.buildTree(rightPr, rightIn)
        
        return root

        # EXAMPLE
        # =================
        # LEVEL 0 CALL
        #           root
        #             |
        # preorder = [4, 6,1,7, 5,2]
        # inorder  = [1,6,7, 4, 5,2]
        #                    |
        #                   root   
        #                                    ___4___
        #                                   /       \
        #  inorder  subtrees:         [1,6,7]       [2,5]
        #  preorder subtree:          [6,1,7]       [5,2]
        # =================
        # LEVEL 1 CALLS
        #           root           root
        #             |             |  
        # preorder = [6, 1, 7],    [5, 2]   (note each subtree's preorder and inorder have same 
        # inorder  = [1, 6, 7],    [2, 5]    elements, just different ordering.)
        #                |             |
        #               root         root 
        #                                  ____4____
        #                                 /         \
        #                               _6_          5_ 
        #                              /   \        /    
        #  inorder  subtrees:         [1]  [7]    [2]
        #  preorder subtrees:         [1]  [7]    [2]
        # =================
        # LEVEL 3 CALLS 
        #
        #                                  ____4____
        #                                 /         \
        #                               _6_          5
        #                              /   \        /    
        #                             1     7      2