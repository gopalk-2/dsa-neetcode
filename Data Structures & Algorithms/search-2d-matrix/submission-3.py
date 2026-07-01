class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x=[]
        for item in matrix:
            x+=item
        lo=0
        high=len(x)-1
        while lo<=high:
            mid=(lo+high)//2
            if x[mid]==target:
                return True
            if target > x[mid]:
                lo=mid+1
            else:
                high=mid-1
        return False        