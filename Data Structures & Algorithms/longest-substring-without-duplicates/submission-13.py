class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longestLen = 0
        characters = set()
        length = 0
        i = 0 # left bound
        for j in range(len(s)): # right bound
            while s[j] in characters:
                characters.remove(s[i])
                i += 1
                length -= 1
            characters.add(s[j])
            length += 1
            longestLen = max(length, longestLen)
        
        return longestLen
