class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj={i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited=set()
        def dfs(i):
            stack=[(i,-1)]
            visited.add(i)
            while stack:
                node,prev=stack.pop()
                for item in adj[node]:
                    if item not in visited:
                        visited.add(item)
                        stack.append((item,node))
                    elif item!=prev:
                        return False
            return True
        
        if not dfs(0):
            return False
        return len(visited) == n

        
        
        