class Solution:
    def trap(self, height: List[int]) -> int:
        
        # prefix: leftToRight
        leftToRight = [None] * len(height)
        leftToRight[0] = height[0]
        for i in range(1, len(height)):
            leftToRight[i] = max(leftToRight[i-1], height[i])
            print(leftToRight[i])
        
        # suffix: rightToLeft
        rightToLeft = [None] * len(height)
        rightToLeft[-1] = height[-1]
        for j in range(len(height)-2, -1, -1):
            rightToLeft[j] = max(rightToLeft[j+1], height[j])
            #print(rightToLeft[j])
        # stored water = min(prefix[i], suffix[i])
        totalWater = 0
        for k in range(len(height)):
            totalWater += min(leftToRight[k], rightToLeft[k]) - height[k]
            
            
        
        return totalWater