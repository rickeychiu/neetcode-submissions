import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freqDict = {} # store as {'X' : 3}
        heap = [] # use heap to keep track of tasks, lead with frequency
        # (more of the same task should be scheduled more often)
        # store as like [-3, [2, 'X'] ]
        for task in tasks:

            if task not in freqDict:
                freqDict[task] = 0
            freqDict[task] += 1
            

        for task, freq in freqDict.items():
            heapq.heappush(heap, [-freq, task])

        queue = deque() # tasks on cooldown, [timeLastRan, task]
        time = 0

        while len(heap) > 0 or len(queue) > 0:

            # see if cooldown task can return to heap
            while len(queue) > 0 and time - queue[0][0] > n:
                heapq.heappush(heap, queue.popleft()[1])

            if len(heap) > 0:
                # run most frequent avaliable task
                task = heapq.heappop(heap)
                # decrease remaining count
                task[0] += 1
                if task[0] < 0: # if there's still copies left, put into cooldown
                    queue.append([time, task])
           
                # idle time

            time += 1
        
        return time
