class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=sorted(nums)
        self.k=k
        
    def add(self, val: int) -> int:
        i=0
        while i<len(self.nums):
            if self.nums[i]<val:
                i+=1
                continue
            elif self.nums[i]>=val:
                break
        self.nums.insert(i,val)
        print(self.nums)
        return sorted(self.nums,reverse=True)[self.k-1]

        
