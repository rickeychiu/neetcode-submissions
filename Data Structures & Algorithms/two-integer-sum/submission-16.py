class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # {number : index}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in seen:
                return [seen[target - num], i]
            else:
                seen[num] = i
        
        return [-1, -1]