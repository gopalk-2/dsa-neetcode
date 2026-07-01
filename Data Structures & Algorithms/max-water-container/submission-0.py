class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_amount=float("-inf")
        i,j=0,n-1
        while i<j:
            width=j-i
            height=min(heights[j],heights[i])
            max_amount=max(height*width,max_amount)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_amount
        