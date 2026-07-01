class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        x=[-i for i in nums]
        heapq.heapify(x)
        for _ in range(k-1):
            heapq.heappop(x)
        return -x[0]
        