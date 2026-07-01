class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c=nums1+nums2
        c.sort()
        is_odd= True if len(c)%2 !=0 else False
        if not c:
            return float(0)
        if is_odd:
            index=int((len(c)+1)/2)-1
            return float(c[index])
        else:
            index1=int(len(c)/2)-1
            index2=index1+1
            return (c[index1]+c[index2])/2

        