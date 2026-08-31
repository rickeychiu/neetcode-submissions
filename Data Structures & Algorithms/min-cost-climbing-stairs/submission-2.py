class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) <= 2:
            return min(cost[1], cost[0])
        dp = [None] * (len(cost) + 1)

        dp[0] = 0
        dp[1] = 0

        # dp[i] represents the min cost to reach that staircase
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[len(cost)]