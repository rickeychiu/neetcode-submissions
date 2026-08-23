class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # iterate through unique numbers,
        # if the num - 1 doesn't exist, it's the start
        # of a sequence
        # use a while loop to see how many consecutive numbers
            # num + 1, num + 2 exist
        
        s = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                longest = max(length, longest)

        return longest

        