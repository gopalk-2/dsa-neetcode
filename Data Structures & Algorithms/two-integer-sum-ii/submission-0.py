class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        n=len(numbers)
        i=0
        j=n-1
        while i<n:
            while j>i:
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                j-=1
            i+=1
            j=n-1

        