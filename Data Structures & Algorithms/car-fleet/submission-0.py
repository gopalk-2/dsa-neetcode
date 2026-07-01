class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x=list(zip(position,speed))
        x.sort()
        count=0
        max_time=0
        for i,j in reversed(x):
            t=(target-i)/j
            if t>max_time:
                count+=1
                max_time=t
        return count
        