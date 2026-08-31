class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        # dp[i] is the max amount of money you can rob from houses 0 through i
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # at each house, don't rob the house = keep dp[i-1],
            # if you rob the house = nums[i] + dp[i-2]
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
        return dp[-1]