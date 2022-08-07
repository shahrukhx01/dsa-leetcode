# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.answer = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return self.maxDepthHelper(root,0)


    def maxDepthHelper(self,node,depth):

        if not node:
            return depth


        left = self.maxDepthHelper(node.left,depth+1)

        right = self.maxDepthHelper(node.right,depth+1)

        return max(left,right)
