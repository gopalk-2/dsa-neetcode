class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(i,remaining,path):
            if remaining==0:
                res.append(path.copy())
                return
            if i == len(nums):
                return
            if nums[i]<=remaining:
                path.append(nums[i])
                dfs(i,remaining-nums[i],path)
                path.pop()
            dfs(i+1,remaining,path)
        dfs(0,target,[])
        return res