class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(i,curr_sum):
            if (i,curr_sum) in memo:
                return memo[(i,curr_sum)]
            if i==len(nums):
                return 1 if curr_sum==target else 0
            positive=dfs(i+1,curr_sum+nums[i])
            negative=dfs(i+1,curr_sum-nums[i])
            memo[(i,curr_sum)]=positive + negative
            return memo[(i,curr_sum)]
        return dfs(0,0)
        