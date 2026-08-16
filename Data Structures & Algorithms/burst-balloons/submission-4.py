     
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        memo = {}

        def dfs(left, right):

            if right - left <= 1:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            res = 0

            for k in range(left + 1, right):

                coins = (
                    dfs(left, k)
                    + dfs(k, right)
                    + nums[left] * nums[k] * nums[right]
                )

                res = max(res, coins)

            memo[(left, right)] = res
            return res

        return dfs(0, len(nums) - 1)
        