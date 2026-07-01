class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        total_left=(m+n+1)//2
        l,h=0,m
        while l<=h:
            i=(l+h)//2
            j=total_left-i
            left1=nums1[i-1] if i>0 else float("-inf")
            right1=nums1[i]  if i < m else float("inf")
            left2=nums2[j-1] if j >0 else float("-inf")
            right2=nums2[j]  if j<n else float("inf")
            if left1 <= right2 and left2 <= right1:
                if (m+n) % 2 == 1:
                    return float(max(left1,left2))
                    
                else:
                    return (min(right1,right2)+max(left1,left2))/2.0
            elif left1>right2:
                h=i-1
            else:
                l=i+1 