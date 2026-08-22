class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqList = {}
        for num in nums:
            if num in freqList:
                freqList[num] += 1
            else:
                freqList[num] = 1

        sortedList = []
        for num, frequency in freqList.items():
            sortedList.append( [frequency, num] )
        sortedList.sort(reverse=True)
        
        answer = []
        for i in range(k):
            answer.append(sortedList[i][1])

        return answer
        