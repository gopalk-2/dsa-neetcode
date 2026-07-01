class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        for i in range(n-1):
            j=i+1
            count=1
            for item in temperatures[j:]:
                if item<=temperatures[i]:
                    count+=1
                elif item>temperatures[i]:
                    res[i]=count
                    break
        return res
        