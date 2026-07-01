class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[-i for i in stones]
        heapq.heapify(h)
        while len(h)>1:
            x=-heapq.heappop(h)
            y=-heapq.heappop(h)
            if x>y:
                heapq.heappush(h,-(x-y))
            elif y>x:
                heapq.heappush(h,-(y-x))
            
        if not h:
            return 0
        else:
            return -h[0]       