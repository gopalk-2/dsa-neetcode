class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        lmax=height[left]
        rmax=height[right]
        res=0
        while left<=right:
            if lmax<rmax:
                if lmax>height[left]:
                    res+=lmax- height[left]
                
                lmax=max(lmax,height[left])
                left+=1
            else:
                if rmax>height[right]:
                    res+=rmax-height[right]
                
                rmax=max(rmax,height[right])
                right-=1
        return res
        