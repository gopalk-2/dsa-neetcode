class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            stack=[(r,c)]
            while stack:
                x,y=stack.pop()
                if x<0 or y<0 or x>=rows or y>=cols or grid[x][y]=='0':
                    continue
                grid[x][y]='0'
                stack.append((x+1,y))
                stack.append((x-1,y))
                stack.append((x,y+1))
                stack.append((x,y-1))
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    dfs(r,c)
                    count+=1
        return count
                
                
