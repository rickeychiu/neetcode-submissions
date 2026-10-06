class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def exploreDFS(i: int, j: int) -> None:

            # check if position is out of bounds
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            # check if it's water or already visited
            if grid[i][j] == "0" or grid[i][j] == "2":
                return
            
            # make the current oen visited
            grid[i][j] = "2"

            # recursively call the 4 directions
            exploreDFS(i-1, j)
            exploreDFS(i+1, j)
            exploreDFS(i, j+1)
            exploreDFS(i, j-1)
        
        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islandCount += 1
                    exploreDFS(i, j)
        return islandCount
        