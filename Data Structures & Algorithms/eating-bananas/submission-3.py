class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            print(mid)
            total=0
            for i in piles:
                if mid!=0:
                    total+=math.ceil(i/mid)
            if total>h:
                low=mid+1
            else:
                high=mid-1
        return low



        