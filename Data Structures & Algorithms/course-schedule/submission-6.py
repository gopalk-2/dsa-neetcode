class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            hmap[j].append(i)
        state=[0]*numCourses
        def hasCycle(course):
            if state[course]==1:
                return True
            if state[course]==2:
                return False
            state[course]=1
            for nei in hmap[course]:
                if hasCycle(nei):
                    return True
            state[course]=2
        for c in range(numCourses):
            if hasCycle(c):
                return False
        return True
        