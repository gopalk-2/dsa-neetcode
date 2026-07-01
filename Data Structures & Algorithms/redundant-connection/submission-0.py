class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        def dfs(visited,src,target):
            if src==target:
                return True
            visited.add(src)
            for nei in graph[src]:
                if nei not in visited:
                    if dfs(visited,nei,target):
                        return True
            return False
        
        for u,v in edges:
            visited=set()
            if u in graph and v in graph and dfs(visited,u,v):
                return [u,v]
            graph[u].append(v)
            graph[v].append(u)

        