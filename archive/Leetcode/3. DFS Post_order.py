# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        done = False
        current = root
        s1,s2,result = [],[],[]
        s1.append(root)

        while s1:
            node = s1.pop()
            s2.append(node)
            if node:
                if node.left:
                    s1.append(node.left)

                if node.right:
                    s1.append(node.right)

        while s2:
            out = s2.pop()
            if out:
                result.append(out.val)
        return result
                    
