class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]
        n=len(nums)
        used=[False]*n
        def dfs(curr):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            for i in range(n):
                if used[i]==False:
                    used[i]=True
                    curr.append(nums[i])
                    dfs(curr)
                    curr.pop()
                    used[i]=False
        dfs([])
        return res

                

        