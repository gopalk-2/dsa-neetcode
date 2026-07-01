class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(numCourses)}
        in_degree=[0]*numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            in_degree[a]+=1
        queue=deque([i for i in range(numCourses) if in_degree[i]==0])
        topo=[]
        while queue:
            node=queue.popleft()
            topo.append(node)
            for nei in adj[node]:
                in_degree[nei]-=1
                if in_degree[nei]==0:
                    queue.append(nei)
                   
        if len(topo)!=numCourses:
            return []
        else:
            return topo
        