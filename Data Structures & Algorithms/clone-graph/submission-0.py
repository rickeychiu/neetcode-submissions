"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return None
        
        # store as {original : new}
        copies = {}
        def dfs(curr):
            if curr in copies:
                return copies[curr]
            
            clone = Node(curr.val)
            copies[curr] = clone

            for nb in curr.neighbors:
                clone.neighbors.append(dfs(nb))
            
            return clone
        
        return dfs(node)


            