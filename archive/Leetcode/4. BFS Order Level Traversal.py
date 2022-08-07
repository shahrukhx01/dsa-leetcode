# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Queue:
    def  __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = Queue()
        queue.enqueue(root)
        result,temp = [],[]

        while queue.size() > 0:

            node_count = queue.size()
            while node_count > 0:
                out = queue.dequeue()

                temp.append(out.val)
                node_count  -= 1
                if out.left:
                    queue.enqueue(out.left)
                if out.right:
                    queue.enqueue(out.right)


            result.append(temp)
            temp = []
        print(result)
        return result













        
