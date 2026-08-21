class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        for char in s:

            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1

        for char in t:

            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1
        
        if dict1 == dict2:
            return True
        return False
        
        