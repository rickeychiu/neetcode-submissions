# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # use BFS, separate by layer, extract the rightmost one in the layer
        answer = []

        if root is None:
            return []
        
        q = deque([root])

        while q:
            level = []
            
            for i in range(len(q)):

                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            answer.append(level[-1])
        
        return answer
            

        