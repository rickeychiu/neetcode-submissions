class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []

        returnArr = []
        nums.sort()
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]: #dupe
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    returnArr.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: #dupe
                        j += 1
                    while j < k and nums[k] == nums[k+1]: #dupe
                        k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        
        return returnArr
