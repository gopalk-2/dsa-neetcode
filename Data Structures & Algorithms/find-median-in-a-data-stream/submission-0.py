class MedianFinder:
    def __init__(self):
        self.nums=[]
        
    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
        else:
            i=0
            while i<len(self.nums):
                if self.nums[i] >=num:
                    break
                i+=1
            self.nums.insert(i,num)
        
    def findMedian(self) -> float:
        n=len(self.nums)
        if n%2 != 0:
            return self.nums[(n-1)//2]
        else:
            i1=n//2-1
            i2=i1+1
            return (self.nums[i1]+self.nums[i2])/2
        
        