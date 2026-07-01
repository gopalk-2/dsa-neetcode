# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        idx_map={ val:i for i,val in enumerate(inorder)}
        pre_idx=0

        def build(in_left,in_right):
            nonlocal pre_idx
            if in_left>in_right:
                return None
            root_val=preorder[pre_idx]
            pre_idx+=1
            root=TreeNode(root_val)
            idx=idx_map[root_val]
            root.left=build(in_left,idx-1)
            root.right=build(idx+1,in_right)

            return root
        return build(0,len(inorder)-1)
        