class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x={}
        for i in nums:
            if i not in x:
                x[i]=0
            x[i]+=1
        s=dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
        res=[]
        i=0
        for key in s:
            if i ==k:
                break
            res.append(key)
            i+=1
            
        return res