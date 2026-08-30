import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y: #stones are destroyed
                continue
            elif x < y: # stone x is destroyed, y is now y-x
                heapq.heappush(heap, -(y - x))
            else:
                heapq.heappush(heap, -(x - y))
        
        if len(heap) == 1:
            return -heap[0]
        else:
            return 0
        