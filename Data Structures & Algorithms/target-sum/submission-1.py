class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(i,curr):
            if (i,curr) in memo:
                return memo[(i,curr)]
            if i==len(nums):
                if curr==target:
                    return 1
                else:
                    return 0
            
            positive=dfs(i+1,curr+nums[i])
            negative=dfs(i+1,curr-nums[i])
            memo[(i,curr)]=positive +negative
            return memo[(i,curr)]
        return dfs(0,0)
