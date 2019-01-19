# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = list()
        current = root
        result = list()
        done = False

        while not done:
            if current:
                s.append(current)
                current = current.left
            else:
                if len(s) > 0:
                    out = s.pop()
                    result.append(out.val)
                    current = out.right
                else:
                    done = True
        return result
                
