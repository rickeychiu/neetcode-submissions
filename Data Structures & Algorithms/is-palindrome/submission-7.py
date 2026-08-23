class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) <= 1:
            return True

        cleanedString = ""
        # clean the string first
        for ch in s:
            if ch.isalnum():
                if ch.isalpha():
                   cleanedString += ch.lower()
                else:
                    cleanedString += ch
        
        i = 0
        j = len(cleanedString) - 1

        while i < j:
            if cleanedString[i] != cleanedString[j]:
                return False
            i += 1
            j -= 1
        
        return True
        