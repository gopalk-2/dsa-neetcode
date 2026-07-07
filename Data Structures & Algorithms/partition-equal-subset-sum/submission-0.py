class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2==1:
            return False
        half=total_sum//2
        memo={}
        def dfs(i,target):
            if target==0:
                return True
            if len(nums)==i:
                return False
            if (i,target) in memo:
                return memo[(i,target)]
            take=dfs(i+1,target-nums[i])
            skip=dfs(i+1,target)
            memo[(i,target)]=take or skip
            return  memo[(i, target)]
        return dfs(0,half)
        