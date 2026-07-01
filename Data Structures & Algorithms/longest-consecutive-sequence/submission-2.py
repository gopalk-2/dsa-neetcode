class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        s=sorted(nums)
        num=s[0]
        res=[num]
        current_res=[num]
        for i in range(1,len(nums)):
            if s[i]==num+1:
                current_res.append(s[i])
                num=s[i]
            elif s[i]==num:
                continue
            else:
                num=s[i]
                current_res=[num]
            if len(current_res)>len(res):
                res=current_res
                
        return len(res)

        