class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==m-1 and j==n-1:
                return 1
            if i>m-1 or j >n-1:
                return 0
            ways=dfs(i+1,j)+dfs(i,j+1)
            memo[(i,j)]=ways
            return ways
        return dfs(0,0)
