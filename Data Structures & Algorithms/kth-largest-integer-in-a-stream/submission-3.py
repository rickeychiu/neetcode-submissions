import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.heap = []
        self.k = k
        for n in nums:
            heapq.heappush(self.heap, -n)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, -val)

        popped = []
        for _ in range(self.k):
            popped.append(heapq.heappop(self.heap))

        for num in popped:
            heapq.heappush(self.heap, num)

        return -popped[-1]
