from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # do BFS, initalize queue with all rotten oranges to start
        q = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append( (r, c, 0)) # position + time
                elif grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        while q: 
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.popleft()
                r = node[0]
                c = node[1]
                t = node[2]
                time = max(time, t)
                grid[r][c] = 2
                if self.canExpandPos(grid, r + 1, c):
                    fresh -= 1
                    grid[r+1][c] = 2
                    q.append((r+1, c, t+1))
                if self.canExpandPos(grid, r - 1, c):
                    fresh -= 1
                    grid[r-1][c] = 2
                    q.append((r-1, c, t+1))
                if self.canExpandPos(grid, r, c + 1):
                    fresh -= 1
                    grid[r][c+1] = 2
                    q.append((r, c+1, t+1))
                if self.canExpandPos(grid, r, c - 1):
                    fresh -= 1
                    grid[r][c-1] = 2
                    q.append((r, c-1, t+1))
        
        return time if fresh == 0 else -1

    

    def canExpandPos(self, grid: List[list[int]], r: int, c: int) -> bool:
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return False
        return grid[r][c] == 1

        
