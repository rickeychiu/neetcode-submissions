class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        freqList1 = {}
        for ch in s1:
            if ch in freqList1:
                freqList1[ch] += 1
            else:
                freqList1[ch] = 1
        
        freqList2 = {}    
        # use sliding window to keep track of window len(s1)
        
        # initalize the ones already in the window
        for k in range(len(s1)):
            ch = s2[k]
            if ch in freqList2:
                freqList2[ch] += 1
            else:
                freqList2[ch] = 1

        i = 0
        # now move the window across
        for j in range(len(s1), len(s2)):

            # first check if the current state contains the permutation
            if freqList1 == freqList2:
                return True

            # if it doesn't, then let's move everything up
            # remove left character
            freqList2[s2[i]] -= 1
            if freqList2[s2[i]] == 0:
                del freqList2[s2[i]] # to keep 0 entrys clean, so i can == above
            ch = s2[j]
            if ch in freqList2:
                freqList2[ch] += 1
            else:
                freqList2[ch] = 1
            i += 1
           

        return freqList1 == freqList2


            
