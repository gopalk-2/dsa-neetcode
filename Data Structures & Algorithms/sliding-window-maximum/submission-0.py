from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        res=[]
        window=deque()
        for i in range(k):
            window.append(nums[i])
        res.append(max(window))
        for r in range(k,len(nums)):
            window.popleft()
            window.append(nums[r])
            res.append(max(window))
            l+=1
        return res
        