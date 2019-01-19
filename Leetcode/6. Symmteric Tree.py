# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetricHelper(root.left,root.right)

    def isSymmetricHelper(self,nodeA,nodeB):
        if not nodeA and not nodeB:
            return True

        if not nodeA and  nodeB:
            return False

        if nodeA and  not nodeB:
            return False

        if nodeA.val != nodeB.val:
            return False

        return self.isSymmetricHelper(nodeA.left,nodeB.right) and self.isSymmetricHelper(nodeA.right,nodeB.left)
