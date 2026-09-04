from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # use breadth first search from the chests
        # first, add every treasure to the queue
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        distance = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                directions = [ (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1) ]

                for newI, newJ in directions:

                    # bounds check
                    if newI < 0 or newJ < 0 or newI >= len(grid) or newJ >= len(grid[0]):
                        continue

                    # only visit unvisited land
                    if grid[newI][newJ] != 2147483647:
                        continue

                    grid[newI][newJ] = distance + 1
                    q.append((newI, newJ))

            distance += 1
