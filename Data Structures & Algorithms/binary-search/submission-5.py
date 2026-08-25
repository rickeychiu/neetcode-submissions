class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # numbers already sorted
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # too small
                i = mid + 1
            elif nums[mid] > target: # too big
                j = mid - 1
        
        return -1