# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        # Recursively invert
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        # Swap children
        root.left, root.right = root.right, root.left
        
        return root