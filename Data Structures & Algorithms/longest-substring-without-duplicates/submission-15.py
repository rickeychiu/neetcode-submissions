class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        i = 0
        maxLen = 0
        for j in range(len(s)):

            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(s[j])
            maxLen = max(len(seen), maxLen)
        
        return maxLen