# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count=0
        stack=[(root,root.val)]
        while stack:
            node,maxSoFar=stack.pop()
            if node.val>=maxSoFar:
                count+=1
            newMax=max(maxSoFar,node.val)
            if node.left:
                stack.append((node.left,newMax))
            if node.right:
                stack.append((node.right,newMax))
        return count


        