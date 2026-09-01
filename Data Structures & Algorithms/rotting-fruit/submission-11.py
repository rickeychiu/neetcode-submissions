from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotted = []
        freshCount = 0
        q = deque()
        # find all inital rotted fruit
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append( (i, j))
                if grid[i][j] == 1:
                    freshCount += 1
        
        # a BFS would be good for this

        time = 0
        while q and freshCount > 0:
            # each level is one unit in time
            levelSize = len(q)
            for _ in range(levelSize):
                
                i, j = q.popleft() # pop here
                
                if self.validSpreadPosition(i+1, j, grid):
                    grid[i+1][j] = 2
                    q.append( (i+1, j) )
                    freshCount -= 1
                if self.validSpreadPosition(i-1, j, grid):
                    grid[i-1][j] = 2
                    q.append( (i-1, j) )
                    freshCount -= 1
                if self.validSpreadPosition(i, j+1, grid):
                    grid[i][j+1] = 2
                    q.append( (i, j+1) )
                    freshCount -= 1
                if self.validSpreadPosition(i, j-1, grid):
                    grid[i][j-1] = 2
                    q.append( (i, j-1) )
                    freshCount -= 1
                
            
            time += 1
        
        if freshCount > 0:
            return -1

        return time




    def validSpreadPosition(self, i: int, j: int, grid: List[List[int]]) -> bool:
        if i < 0 or j < 0:
            return False
        if i >= len(grid) or j >= len(grid[0]):
            return False
        if grid[i][j] == 0 or grid[i][j] == 2:
            return False
        
        return True
        