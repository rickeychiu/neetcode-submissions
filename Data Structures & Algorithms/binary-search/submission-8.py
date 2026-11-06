class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # already sorted, begin binary search
        i = 0 # left bound
        j = len(nums) - 1 # right bound

        while i <= j:

            mid = (i + j) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # cut leftside
                i = mid + 1
            else: # cut rihghtside
                j = mid - 1
        
        return -1
            