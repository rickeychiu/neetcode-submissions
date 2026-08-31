class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def explore(x: int, y: int, grid: List[List[str]]) -> None:

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return

            if grid[x][y] == "0" or grid[x][y] == "2":
                return
            
            # mark this one as visited
            grid[x][y] = "2"

            explore(x-1, y, grid)
            explore(x+1, y, grid)
            explore(x, y+1, grid)
            explore(x, y-1, grid)

        
        islands = 0
        # mark '2' for visited land
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    explore(i, j, grid)
        
        return islands

        