# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        head = root
        while head:

            if head.val > p.val and head.val > q.val: # go left
                head = head.left
            elif head.val < p.val and head.val < q.val: #go right
                head = head.right
            else: # that's the diverging part
                return head
        
        return None
            