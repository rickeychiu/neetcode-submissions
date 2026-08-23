class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if len(numbers) == 2:
            return [1,2]
        
        i = 0
        j = len(numbers) - 1

        while i < j:
            testSum = numbers[i] + numbers[j]
            
            if testSum == target:
                return [i + 1, j+ 1]
            elif testSum < target: # if it's too small, move left up
                i += 1
            else: # if it's too large, move right down
                j -= 1
        
        return [-1, -1]
            