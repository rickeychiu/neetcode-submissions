class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) < 1:
            return []

        leftToRightProducts = [None] * len(nums)
        leftToRightProducts[0] = nums[0]
        for i in range(1, len(nums)):
            leftToRightProducts[i] = leftToRightProducts[i-1] * nums[i]


        rightToLeftProducts = [None] * len(nums)
        rightToLeftProducts[-1] = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            rightToLeftProducts[j] = rightToLeftProducts[j+1] * nums[j]

        answerArr = [None] * len(nums)
        answerArr[0] = rightToLeftProducts[1]

        for k in range(1, len(nums) - 1):
            answerArr[k] = leftToRightProducts[k-1] * rightToLeftProducts[k+1]
        
        answerArr[-1] = leftToRightProducts[-2]

        return answerArr
        