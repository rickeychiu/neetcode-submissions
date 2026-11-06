class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freqList1 = {} # {char : freq}
        freqList2 = {} 

        for ch in s:
            if ch not in freqList1:
                freqList1[ch] = 0
            freqList1[ch] += 1
        
        for ch in t:
            if ch not in freqList2:
                freqList2[ch] = 0
            freqList2[ch] += 1
        
        for ch, freq in freqList1.items():
            if ch not in freqList2:
                return False
            if freqList2[ch] != freq:
                return False
        for ch, freq in freqList2.items():
            if ch not in freqList1:
                return False
            if freqList1[ch] != freq:
                return False
        return True
        