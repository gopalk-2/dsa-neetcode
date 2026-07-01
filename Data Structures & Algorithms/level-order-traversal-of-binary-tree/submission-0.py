from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        deq=deque([root])
        res=[]
        while deq:
            length=len(deq)
            level_nodes=[]
            for _ in range(length):
                node=deq.popleft()
                level_nodes.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(level_nodes)
        return res
        