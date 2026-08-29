class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqList = {} # store as {character : frequency}

        maxLength = 0
        maxFreq = 0
        i = 0
        for j in range(len(s)):

            if s[j] in freqList:
                freqList[s[j]] += 1
            else:
                freqList[s[j]] = 1

            
            maxFreq = max(maxFreq, freqList[s[j]])

            length = j - i + 1
            while length - maxFreq > k:

                freqList[s[i]] -= 1
                i += 1
                length -= 1
            
            maxLength = max(maxLength, length)
        
        return maxLength




        