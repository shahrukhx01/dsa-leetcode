# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """


        done = False
        current = root
        s = list()
        result = list()
        while not done:
            if current:
                result.append(current.val)
                s.append(current)
                current = current.left
            else:
                if len(s) > 0:
                    current = s.pop().right
                else:
                    done = True
        return result
