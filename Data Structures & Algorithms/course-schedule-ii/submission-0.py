class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hmap={i:[] for i in range(numCourses)}
        in_degree=[0]*numCourses
        for i,j in prerequisites:
            hmap[j].append(i)
            in_degree[i]+=1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in hmap[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) == numCourses:
            return order
        else:
            return []
        