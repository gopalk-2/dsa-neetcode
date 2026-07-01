class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        min_prod=nums[0]
        res=nums[0]
        for i  in range(1,len(nums)):
            num=nums[i]
            temp_max=max(num,num*max_prod,min_prod*num)
            temp_min=min(num,num*max_prod,min_prod*num)
            max_prod=temp_max
            min_prod=temp_min
            res=max(max_prod,res)
        return res
