class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=[i for i in nums]
        heapq.heapify(self.nums)
        self.k=k
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
        elif val>self.nums[0]:
            heapq.heapreplace(self.nums,val)
        return self.nums[0]
