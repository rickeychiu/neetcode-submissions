class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort so you can use the twoSum algorithm
        nums.sort()

        returnArr = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
        
            while j < k:
                testSum = nums[i] + nums[j] + nums[k]
                if testSum == 0:
                    if [nums[i], nums[j], nums[k]] not in returnArr:
                        returnArr.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif testSum < 0: # if it's too small, move left up
                    j += 1
                else: # if it's too large, move right down
                    k -= 1
        return returnArr
        