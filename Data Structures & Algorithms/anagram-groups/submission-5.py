class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        masterDict = {}
        for word in strs:

            key = []
            for char in word:
                key.append(char)
            
            key.sort()
            keystr = ""
            for char in key:
                keystr += char
            
            if keystr in masterDict:
                masterDict[keystr] += [word]
            else:
                masterDict[keystr] = [word]

        
        return list(masterDict.values())
