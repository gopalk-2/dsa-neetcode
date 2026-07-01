class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            hmap[j].append(i)

        state = [0] * numCourses

        def hasCycle(course):
            stack = [(course, 0)]  # (node, phase)
            while stack:
                node, phase = stack.pop()
                if phase == 0:  # entering
                    if state[node] == 1:  # cycle
                        return True
                    if state[node] == 2:  # already processed
                        continue
                    state[node] = 1
                    stack.append((node, 1))  # exit phase
                    for nei in hmap[node]:
                        stack.append((nei, 0))
                else:  # exiting
                    state[node] = 2
            return False

        for c in range(numCourses):
            if state[c] == 0 and hasCycle(c):
                return False
        return True
