class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        x={}
        res=0
        if not s:
            return res
        for r in range(len(s)):
            if s[r] not in x:
                x[s[r]]=1
            else:
                x[s[r]]+=1
            while (r-l)+1-max(x.values())>k:
                x[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res


        