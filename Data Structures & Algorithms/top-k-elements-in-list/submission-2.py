class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        buckets=[[] for _ in range(len(nums)+1)]
        for i,j in count.items():
            buckets[j].append(i)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res)==k:
                    return res


        