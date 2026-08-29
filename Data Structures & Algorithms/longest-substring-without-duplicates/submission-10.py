class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charsInside = set()
        maxLength = 0
        i = 0
        length = 0
        for j in range(len(s)):
            
            while s[j] in charsInside:
                charsInside.remove(s[i])
                i += 1
                length -= 1
            
            charsInside.add(s[j])
            length += 1
            maxLength = max(maxLength, length)

        return maxLength
        