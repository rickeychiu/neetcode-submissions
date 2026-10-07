class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        
        left = 0
        charsInside = set()
        charsInside.add(s[0])
        maxLength = 1
        for right in range(1, len(s)):

            while s[right] in charsInside:
                charsInside.remove(s[left])
                left += 1
            charsInside.add(s[right])
            maxLength = max(maxLength, len(charsInside))
        
        return maxLength

