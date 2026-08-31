class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1 and n == 1:
            return 1
        
        dp = [[-1] * n] * m
        # dp[i][j] represents the amount of unique paths you can take to get to this spot
        # can only move down and right, so everything along the margins is 1
        for i in range(m):
            for j in range(n):

                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]


        return dp[m-1][n-1]
        