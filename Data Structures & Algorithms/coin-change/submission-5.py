class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        if amount ==0:
            return 0
        def dfs(target):
            if target in memo:
                return memo[target]
            if target==0:
                return 0
            if target <0:
                return float("inf")
            count =float("inf")
            for coin in coins:
                count=min(count,1+dfs(target-coin))
            memo[target]=count
            return count
        ans=dfs(amount)
        return -1 if ans== float("inf") else ans