class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i <= 0 or j <= 0:
                return 0
            if i == 1 and j == 1:
                return 1
            memo[(i,j)] = dfs(i - 1, j) + dfs(i, j - 1)
            return memo[(i,j)]
        return dfs(m, n)
