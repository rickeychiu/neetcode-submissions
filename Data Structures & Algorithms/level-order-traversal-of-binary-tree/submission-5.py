# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        returnList = []
        if root is None:
            return []
        q = deque([root])
        while q:
            level = []
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            returnList.append(level)
        
        return returnList
        