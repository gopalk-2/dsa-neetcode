class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=set()
        def dfs(src):
            visited.add(src)
            stack=[src]
            while stack:
                node=stack.pop()
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
        count=0
        for i in adj:
            if int(i) not in visited:
                dfs(i)
                count+=1
        return count
        