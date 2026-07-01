class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        x=sorted(count.items(),key=lambda item:item[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(x[i][0])
        return res

        