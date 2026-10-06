class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                answer.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # undo
            subset.pop()

            # don't include nums[i]
            backtrack(i + 1)
        
        backtrack(0)
        return answer
        