class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def exploreDFS(i: int, j: int) -> int:
            
            # if out of bounds
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            # if visited or water
            if grid[i][j] == 0 or grid[i][j] == 2:
                return 0
            # mark current node as visited
            grid[i][j] = 2
            # traverse in all directions
            return 1 + exploreDFS(i+1, j) + exploreDFS(i-1, j) + exploreDFS(i, j+1) + exploreDFS(i, j-1)

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandArea = exploreDFS(i, j)
                    maxArea = max(maxArea, islandArea)
        return maxArea