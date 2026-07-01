# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum=float("-inf")

        def dfs(root):
            if not root:
                return 0
            leftMax=max(0,dfs(root.left))
            rightMax=max(0,dfs(root.right))
            current_max=root.val+leftMax+rightMax
            self.max_sum=max(current_max,self.max_sum)

            return root.val+max(leftMax,rightMax)
        dfs(root)
        return self.max_sum

        