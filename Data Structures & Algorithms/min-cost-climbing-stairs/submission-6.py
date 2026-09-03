class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 0:
            return 0
        if len(cost) <= 1:
            return cost[0]
        
        dp = [None] * (len(cost) +1)
        # dp[i] = the min cost of reaching the n'th staircase
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost) + 1):
            dp[i] = min(cost[i-2] + dp[i-2], cost[i-1] + dp[i-1])
        
        return dp[len(cost)]