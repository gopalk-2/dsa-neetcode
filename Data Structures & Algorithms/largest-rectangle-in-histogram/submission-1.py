class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        max_area=0
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                if not stack:
                    w=i
                else:
                    w=i-stack[-1]-1
                max_area=max(max_area,h*w)
            stack.append(i)
        while stack:
            h=heights[stack.pop()]
            if not stack:
                w=n
            else:
                w=n-stack[-1]-1
            max_area=max(max_area,h*w)
        return max_area
                
        