class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def explore(x: int, y: int, grid: List[List[str]]) -> int:

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 0

            if grid[x][y] == 0 or grid[x][y] == 2:
                return 0
            
            # mark this one as visited
            grid[x][y] = 2

            return 1 + explore(x-1, y, grid) + explore(x+1, y, grid) + explore(x, y+1, grid) + explore(x, y-1, grid)

        
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = explore(i, j, grid)
                    maxArea = max(maxArea, area)

        return maxArea