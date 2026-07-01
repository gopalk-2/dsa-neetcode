class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x={}
        for num in nums:
            if num not in x:
                x[num]=0
            x[num]+=1
        for i in x.values():
            if i>1:
                return True
        return False
        