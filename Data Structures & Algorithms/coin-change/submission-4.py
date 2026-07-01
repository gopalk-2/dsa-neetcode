class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def helper(target):
            if target in memo:
                return memo[target]

            if target == 0:
                return 0
            ans = float('inf')

            for coin in coins:
                if coin <=target:
                    ans = min(ans, 1 + helper(target - coin))

            memo[target] = ans
            return ans

        res = helper(amount)
        return res if res != float('inf') else -1