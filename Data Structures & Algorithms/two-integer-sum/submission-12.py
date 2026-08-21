class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # can't sort because indices have to be preserved

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [-1, -1]

