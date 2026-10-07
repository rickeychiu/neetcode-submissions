import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = [] # store as (frequency, value)
        dic = dict() # store as {value : frequency}
        answer = []

        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        
        for value, frequency in dic.items():
            heapq.heappush(heap, (-frequency, value))

        for i in range(k):
            frequency, value = heapq.heappop(heap)
            answer.append(value)
        
        return answer
        

        