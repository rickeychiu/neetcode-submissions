class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {} # store as { node1 : node2, node3 }
     
        # node 1 must be taken before node2 and node3
        for course, prereq in prerequisites:
            if prereq not in adjList:
                adjList[prereq] = []
            adjList[prereq].append(course)
        
        # now check if it's valid by checking if there are no cycles
        states = {} # store as { node : state }
        # state (None) = unvisited, = 1 means exploring, = 2 means visited
        order = []
        def hasCycle(node):
            if node in states:
                if states[node] == 1:
                    return True  # cycle, current exploration sees same node
                if states[node] == 2:
                    return False # already checked a previous call
            
            states[node] = 1 # mark current unvisited node as exploring
            for nb in adjList.get(node, []):
                if hasCycle(nb):
                    return True
            
            # now, done checking. set everything to 2 for next run
            states[node] = 2
            order.append(node)
            return False

        # run hasCycle from every node
        bestOrder = []
        for node in range(numCourses):
            if hasCycle(node):
                return []

        
        return order[::-1]