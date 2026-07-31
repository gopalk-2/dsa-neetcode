class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return 0

            count = 1
            if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
                count = max(count, 1 + dfs(i + 1, j))

            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                count = max(count, 1 + dfs(i - 1, j))

            if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
                count = max(count, 1 + dfs(i, j + 1))

            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                count = max(count, 1 + dfs(i, j - 1))

            memo[(i, j)] = count
            return count

        max_count = float("-inf")
        for i in range(m):
            for j in range(n):
                max_count = max(max_count, dfs(i, j))

        return max_count

        