class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}
        # [ a, b] means b -> a
        for course, prereq in prerequisites:
            if prereq not in adjList:
                adjList[prereq] = []
            adjList[prereq].append(course)
        # finish building adjList

        # can finish = no cycle
        state = [0] * numCourses
        # 0 = unvisited, 1 = exploring, 2 = unvisited
        def DFSDetectCycle(node: int) -> bool:
            if state[node] == 1:
                return True # current cycle's node
            if state[node] == 2:
                return False 
            state[node] = 1
            for nb in adjList.get(node, []):
                if DFSDetectCycle(nb):
                    return True
            state[node] = 2
            return False
        
        for i in range(numCourses):
            if DFSDetectCycle(i):
                return False
        
        return True