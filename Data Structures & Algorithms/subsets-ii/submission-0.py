class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(i,path):
            if path not in res:
                res.append(path[:])
            for i in range(i,len(nums)):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        dfs(0,[])
        return res
        