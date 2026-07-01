class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        for item in matrix:
            start=0
            end=len(item)-1
            while start<=end:
                mid=(start+end)//2
                if item[mid]==target:
                    return True
                if target>item[0]:
                    start=mid+1
                else:
                    end=mid-1
        return False
