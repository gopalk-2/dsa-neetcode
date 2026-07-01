class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_key(nums,key):
            l,h=0,len(nums)-1
            while l<=h:
                mid=(l+h)//2
                if nums[mid]==key:
                    return True
                elif target<nums[mid]:
                    h=mid-1
                else:
                    l=mid+1
            return False
        for array in matrix:
            if search_key(array,target):
                return True
        return False
        
        