class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        ans=0
        while left<=right:
            mid=(left+right)//2
            hours=sum(math.ceil(i/mid) for i in piles)
            if hours<=h:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
        