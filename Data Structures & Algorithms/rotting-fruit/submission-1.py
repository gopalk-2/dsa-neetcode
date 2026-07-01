class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        fresh_cnt=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                if grid[r][c]==1:
                    fresh_cnt+=1
        if fresh_cnt==0:
            return 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        cnt=0
        while queue:
            r,c,minute=queue.popleft()
            cnt=max(minute,cnt)
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_cnt-=1
                    queue.append((nr, nc,minute+1))
        if fresh_cnt==0:
            return cnt
        else:
            return -1

        