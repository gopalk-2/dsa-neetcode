class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        max_count=0
        def dfs(r,c):
            stack=[(r,c)]
            count=0
            while stack:
                r,c=stack.pop()
                if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or (r,c) in visited:
                    continue
                visited.add((r,c))
                count+=1
                stack.append((r+1,c))
                stack.append((r-1,c))
                stack.append((r,c+1))
                stack.append((r,c-1))
            return count
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]!=0:                  
                    cnt=dfs(r,c)
                    max_count=max(cnt,max_count)
        return max_count

        