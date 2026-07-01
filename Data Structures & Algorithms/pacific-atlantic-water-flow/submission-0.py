class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(source):
            seen=set(source)
            stack=list(source)

            while stack:
                r,c=stack.pop()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if (0<=nr<rows and 0<=nc<cols and (nr,nc) not in seen and heights[nr][nc]>=heights[r][c]):
                        seen.add((nr,nc))
                        stack.append((nr,nc))
            return seen
        
        pac_starts=[(0,c) for c in range(cols)]+ [(r,0) for r in range(rows)]
        atl_starts=[(rows-1,c) for c in range(cols)]+ [(r,cols-1) for r in range(rows)]
        pac=dfs(pac_starts)
        alt=dfs(atl_starts)
        return list(pac & alt)

        