# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        if root is None:
            return []
        answer = []
        q = deque([root])

        while q:
            # at each level, the queue contains exactly the nodes for that level
            level = []
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.popleft()
                level.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            answer.append(level)

        
        return answer
        