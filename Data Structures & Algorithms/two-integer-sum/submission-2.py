class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in x:
                return [x[diff],i]
            if nums[i] not in x:
                x[nums[i]]=i
        