class MedianFinder:
    def __init__(self):
       self.low=[] # max heap
       self.high=[] # min heap 
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.low,-num)

        # check ordering
        if self.low and self.high and -self.low[0]>self.high[0]:
            heapq.heappush(self.high,-heapq.heappop(self.low))
        # check if gap is <1 or greater than >1
        if len(self.low) > len(self.high)+1:
            heapq.heappush(self.high,-heapq.heappop(self.low))
        elif len(self.low)<len(self.high):
            heapq.heappush(self.low,-heapq.heappop(self.high))

        
    def findMedian(self) -> float:
        if len(self.low)>len(self.high):
            return -self.low[0]
        return (-self.low[0]+self.high[0])/2.0
        
        