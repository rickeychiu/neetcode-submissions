import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = [] # store as [distance, [X, Y]]
        
        for x, y in points:
            distance = (x**2 + y**2) ** 0.5
            heapq.heappush(heap, [distance, [x, y]])
        

        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])
        
        return answer