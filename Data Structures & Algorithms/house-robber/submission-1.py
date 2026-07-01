class Solution:
    def rob(self, nums: List[int]) -> int:
        max1=0
        max2=0
        for num in nums:
            temp=max(max1+num,max2)
            max1=max2
            max2=temp
        return max2        
        