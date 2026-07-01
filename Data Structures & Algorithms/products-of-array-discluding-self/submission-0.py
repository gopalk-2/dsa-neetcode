import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(math.prod(nums[0:i])*math.prod(nums[i+1:]))
        return res

        