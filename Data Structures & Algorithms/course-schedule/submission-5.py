class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        state=[0]*numCourses  # unvisited=0 , visiting=1, visited=2
        def hasCycle(course):
            if state[course]==1:
                return True
            if state[course]==2:
                return False
            state[course]=1
            for nei in graph[course]:
                if hasCycle(nei):
                    return True
            state[course]=2
            return False
        for c in range(numCourses):
            if hasCycle(c):
                return False
        return True